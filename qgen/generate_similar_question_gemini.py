import argparse
import os
import re
import yaml
from concurrent.futures import ThreadPoolExecutor

from tqdm import tqdm
from .models.gemini import Gemini

# from .prompt_template import  QGEN_PROMPT
from .utils import dict_to_text, prepare_file, read_jsonl, setup_logger, write_jsonl

logger = setup_logger()

QGEN_PROMPT = """
Given context:
{context}

Question:
{question}

Create 10 similar questions to the given question, which has answer in the given context. 
Put question in the <question></question> tags.

""".strip()


class QAGeneratorGemini:
    def __init__(self, model_name, api_key, **kwargs):
        self.model = Gemini(model_name=model_name, api_key=api_key, **kwargs)

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
        match = re.findall(r"\<question\>(?P<question>[^<]+)\</question\>", response)
        for m in match:
            output.append(m)

        return output

    def build_prompts(self, data, questions):
        # set default prompt template
        prompt_template = QGEN_PROMPT
        prompts = [
            prompt_template.format_map({"context": context, "question": question})
            for context, question in zip(data, questions)
        ]
        return prompts

    def generate(
        self,
        data,
        prompts,
        max_tokens,
        temperature,
        top_p,
        top_k,
        batch_size,
        output_path,
        n_workers=1,
    ):
        sampling_params = {
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
        }

        with ThreadPoolExecutor(max_workers=n_workers) as executor:
            for start_idx in range(0, len(data), batch_size):
                end_idx = min(len(data), start_idx + batch_size)
                responses = tqdm(
                    executor.map(
                        lambda prompt: self.model.generate(prompt, **sampling_params),
                        prompts[start_idx:end_idx],
                    ),
                    total=len(data),
                    initial=start_idx + 1,
                    desc="examples",
                    ncols=0,
                )

                output = []
                for response, context in zip(responses, data[start_idx:end_idx]):
                    output_obj = {}
                    output_obj["context"] = context
                    output_obj["questions"] = self.parse_reponse(response)
                    output.append(output_obj)
                write_jsonl(output, output_path, mode="a", verbose=False)

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
        n_workers=1,
    ):
        data = read_jsonl(input_path, n_examples)
        contexts = [d["pos"][0] for d in data]
        questions = [d["query"] for d in data]
        assert len(contexts) == len(questions)
        logger.info(f"Read {len(contexts)} contexts")

        n_processed = self.check_processed_data(output_path)
        logger.info(f"Found {n_processed} processed contexts")
        contexts = contexts[n_processed:]
        logger.info("Build prompts")
        prompts = self.build_prompts(contexts, questions)
        assert len(prompts) == len(contexts)

        logger.info("Generate question-answer pairs")
        self.generate(
            contexts,
            prompts,
            max_tokens,
            temperature,
            top_p,
            top_k,
            batch_size,
            output_path,
            n_workers,
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model_name", type=str, default="")
    parser.add_argument("-i", "--input_path", type=str, required=True)
    parser.add_argument("-o", "--output_path", type=str, required=True)
    parser.add_argument("-n", "--n_examples", type=int, default=0)
    parser.add_argument("-b", "--batch_size", type=int, default=1000)
    parser.add_argument("--n_workers", type=int, default=16)
    parser.add_argument("--max_tokens", type=int, default=256)
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--top_p", type=float, default=1.0)
    parser.add_argument("--top_k", type=int, default=50)
    args = parser.parse_args()

    # set up logger
    logger.info(f"Config\n{dict_to_text(args, indent=2, sort=False)}")
    api_key = yaml.safe_load(open("secret/gemini.yml"))[args.model_name]["api_key"]
    qa_generator = QAGeneratorGemini(
        model_name=args.model_name, api_key=api_key, wait_time=1.0, max_retry=10
    )
    qa_generator.run(
        input_path=args.input_path,
        output_path=args.output_path,
        n_examples=args.n_examples,
        max_tokens=args.max_tokens,
        temperature=args.temperature,
        top_p=args.top_p,
        top_k=args.top_k,
        batch_size=args.batch_size,
        n_workers=args.n_workers,
    )
