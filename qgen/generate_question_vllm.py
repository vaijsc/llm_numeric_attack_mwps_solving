import argparse
import os
import random
import re

from tqdm import tqdm
from vllm import LLM, SamplingParams

from .prompt_template import  QGEN_PROMPT_CUSTOM, QGEN_PROMPT
from .utils import dict_to_text, prepare_file, read_jsonl, setup_logger, write_jsonl

logger = setup_logger()


class QAGeneratorVLLM:
    def __init__(self, model_path, tensor_parallel_size=1):
        self.model = LLM(model_path, tensor_parallel_size=tensor_parallel_size)
        self.tokenizer = self.model.get_tokenizer()

    def check_processed_data(self, output_path):
        prepare_file(output_path)
        n_processed = 0
        if os.path.isfile(output_path):
            with open(output_path) as f:
                for _ in f:
                    n_processed += 1
        return n_processed

    def parse_reponse(self, response: str) -> list[dict]:
        output = []
        match = re.findall( r"\<question\>(?P<question>[^<]+)\</question\>", response)
        for m in match:
            output.append(m.strip())

        return output

    def create_messages(self, prompt_template, context):
        prompt = prompt_template.format_map(
            {
                "context": context,
            }
        )
        messages = [{"role": "user", "content": prompt}]
        return messages

    def build_prompts(self, data):
        # set default prompt template
        prompt_template = QGEN_PROMPT
        messages_list = [
            self.create_messages(prompt_template, context)
            for context in data
        ]

        prompts = [
            self.tokenizer.apply_chat_template(
                messages, add_generation_prompt=True, tokenize=False
            )
            for messages in messages_list
        ]
        return prompts

    def generate(
        self, data, prompts, max_tokens, temperature, top_p, top_k, batch_size, output_path
    ):
        sampling_params = {
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
        }
        sampling_params = SamplingParams(**sampling_params)

        p_bar = tqdm(total=len(prompts), desc="examples", ncols=0)
        for start_idx in range(0, len(prompts), batch_size):
            end_idx = min(len(prompts), start_idx + batch_size)

            generation_outputs = self.model.generate(
                prompts[start_idx:end_idx], sampling_params, use_tqdm=False
            )
            output = []
            for generation_output, context in zip(
                generation_outputs, data[start_idx:end_idx]
            ):
                output_obj = {}
                output_obj["context"] = context
                output_obj["questions"] = self.parse_reponse(generation_output.outputs[0].text.strip())
                output.append(output_obj)

            write_jsonl(output, output_path, mode="a", verbose=False)
            p_bar.update(end_idx - start_idx)
        p_bar.close()

    def run(
        self,
        input_path,
        output_path,
        n_examples=0,
        max_tokens=256,
        temperature=1.0,
        top_p=1.0,
        top_k=50,
        batch_size=100,
    ):
        contexts = read_jsonl(input_path, n_examples)
        new_contexts = []
        for d in contexts:
            for chunk in d['chunks']:
                new_contexts.append(chunk)
        contexts = new_contexts
        logger.info(f"Read {len(contexts)} contexts")

        n_processed = self.check_processed_data(output_path)
        logger.info(f"Found {n_processed} processed contexts")
        contexts = contexts[n_processed:]

        logger.info("Build prompts")
        prompts = self.build_prompts(contexts)
        assert len(prompts) == len(contexts)

        logger.info("Generate question-answer pairs")
        self.generate(contexts, prompts, max_tokens, temperature, top_p, top_k, batch_size, output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model_path", type=str, default="")
    parser.add_argument("-i", "--input_path", type=str, required=True)
    parser.add_argument("-o", "--output_path", type=str, required=True)
    parser.add_argument("-n", "--n_examples", type=int, default=0)
    parser.add_argument("-b", "--batch_size", type=int, default=1000)
    parser.add_argument("-t", "--tensor_parallel_size", type=int, default=1)
    parser.add_argument("--max_tokens", type=int, default=256)
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--top_p", type=float, default=1.0)
    parser.add_argument("--top_k", type=int, default=50)
    args = parser.parse_args()

    # set up logger
    logger.info(f"Config\n{dict_to_text(args, indent=2, sort=False)}")

    qa_generator = QAGeneratorVLLM(model_path=args.model_path, tensor_parallel_size=args.tensor_parallel_size)
    qa_generator.run(
        input_path=args.input_path,
        output_path=args.output_path,
        n_examples=args.n_examples,
        max_tokens=args.max_tokens,
        temperature=args.temperature,
        top_p=args.top_p,
        top_k=args.top_k,
        batch_size=args.batch_size
    )

