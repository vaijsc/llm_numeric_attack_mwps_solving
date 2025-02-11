import argparse
import re

from tqdm import tqdm
from vllm import LLM, SamplingParams

from .prompt_template import (
    FILTER_CONTEXT_DEPENDENT_PROMPT,
    FILTER_NO_ANSWER_PROMPT,
    ANSWER_PROMPT,
)
from .utils import prepare_file, read_jsonl, setup_logger, write_jsonl

logger = setup_logger()


class QuestionFilter:
    """Select hiquality questions base on similarity score on a corpus of contexts"""

    def __init__(self, model_path, tensor_parallel_size=1):
        self.model = LLM(model_path, tensor_parallel_size=tensor_parallel_size)
        self.tokenizer = self.model.get_tokenizer()

    def get_data(self, input_path, n_example):
        data = read_jsonl(input_path, n_example)
        data = [d for d in data if len(d["questions"]) > 0]

        # convert input triplet (context, question, answer) for easier selection
        cqas = []
        for d in data:
            for question in d["questions"]:
                cqas.append(
                    {
                        "context": d["context"],
                        "question": question,
                    }
                )
        logger.info(f"{len(cqas)} CQ pairs")
        return cqas

    def parse_reponse_verdict(self, response: str) -> list[dict]:
        match = re.search(
            r"\<verdict\>(?P<verdict>[^<]+)\</verdict\>",
            response,
        )
        if match:
            verdict = match.group("verdict").lower().strip()
            return verdict == "true"

        return False

    def build_prompts_filter_context_dependent(self, data):
        prompt_template = FILTER_CONTEXT_DEPENDENT_PROMPT
        messages_list = [
            [
                {
                    "role": "user",
                    "content": prompt_template.format(question=d["question"]),
                }
            ]
            for d in data
        ]

        prompts = [
            self.tokenizer.apply_chat_template(
                messages, add_generation_prompt=True, tokenize=False
            )
            for messages in messages_list
        ]
        return prompts

    def build_prompts_answer(self, data):
        prompt_template = ANSWER_PROMPT
        messages_list = [
            [
                {
                    "role": "user",
                    "content": prompt_template.format(
                        context=d["context"], question=d["question"]
                    ),
                }
            ]
            for d in data
        ]

        prompts = [
            self.tokenizer.apply_chat_template(
                messages, add_generation_prompt=True, tokenize=False
            )
            for messages in messages_list
        ]
        return prompts

    def build_prompts_filter_no_answer(self, data):
        prompt_template = FILTER_NO_ANSWER_PROMPT
        messages_list = [
            [{"role": "user", "content": prompt_template.format(answer=d["answer"])}]
            for d in data
        ]

        prompts = [
            self.tokenizer.apply_chat_template(
                messages, add_generation_prompt=True, tokenize=False
            )
            for messages in messages_list
        ]
        return prompts

    def filter_context_dependent(
        self,
        data,
        max_tokens,
        temperature,
        top_p,
        top_k,
        batch_size,
        output_path="",
        use_tqdm=False,
    ):
        prompts = self.build_prompts_filter_context_dependent(data)
        assert len(prompts) == len(data)

        sampling_params = {
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
        }
        sampling_params = SamplingParams(**sampling_params)

        p_bar = tqdm(total=len(prompts), desc="examples", ncols=0)
        total_output = []
        for start_idx in range(0, len(prompts), batch_size):
            end_idx = min(len(prompts), start_idx + batch_size)

            generation_outputs = self.model.generate(
                prompts[start_idx:end_idx],
                sampling_params,
                use_tqdm=use_tqdm,
            )

            output = []
            for generation_output, d, prompt in zip(
                generation_outputs, data[start_idx:end_idx], prompts[start_idx:end_idx]
            ):
                response = generation_output.outputs[0].text.strip()
                is_context_dependent = self.parse_reponse_verdict(response)
                output_obj = {
                    "context": d["context"],
                    "question": d["question"],
                    "prompt": prompt,
                    "response": response,
                    "is_context_dependent": is_context_dependent,
                }
                output.append(output_obj)

            total_output.extend(output)
            if output_path:
                write_jsonl(output, output_path, mode="a", verbose=False)
            p_bar.update(end_idx - start_idx)
        p_bar.close()

        total_output = [d for d in total_output if not d["is_context_dependent"]]
        return total_output

    def generate_answer(
        self,
        data,
        max_tokens,
        temperature,
        top_p,
        top_k,
        batch_size,
        output_path="",
        use_tqdm=False,
    ):
        prompts = self.build_prompts_answer(data)
        assert len(prompts) == len(data)

        sampling_params = {
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
        }
        sampling_params = SamplingParams(**sampling_params)

        p_bar = tqdm(total=len(prompts), desc="examples", ncols=0)
        total_output = []
        for start_idx in range(0, len(prompts), batch_size):
            end_idx = min(len(prompts), start_idx + batch_size)

            generation_outputs = self.model.generate(
                prompts[start_idx:end_idx],
                sampling_params,
                use_tqdm=use_tqdm,
            )

            output = []
            for generation_output, d, prompt in zip(
                generation_outputs, data[start_idx:end_idx], prompts[start_idx:end_idx]
            ):
                response = generation_output.outputs[0].text.strip()
                output_obj = {
                    "context": d["context"],
                    "question": d["question"],
                    "prompt": prompt,
                    "answer": response,
                }
                output.append(output_obj)

            total_output.extend(output)
            if output_path:
                write_jsonl(output, output_path, mode="a", verbose=False)
            p_bar.update(end_idx - start_idx)
        p_bar.close()

        return total_output

    def filter_no_answer(
        self,
        data,
        max_tokens,
        temperature,
        top_p,
        top_k,
        batch_size,
        output_path="",
        use_tqdm=False,
    ):
        prompts = self.build_prompts_filter_no_answer(data)
        assert len(prompts) == len(data)

        sampling_params = {
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
        }
        sampling_params = SamplingParams(**sampling_params)

        p_bar = tqdm(total=len(prompts), desc="examples", ncols=0)
        total_output = []
        for start_idx in range(0, len(prompts), batch_size):
            end_idx = min(len(prompts), start_idx + batch_size)

            generation_outputs = self.model.generate(
                prompts[start_idx:end_idx],
                sampling_params,
                use_tqdm=use_tqdm,
            )

            output = []
            for generation_output, d, prompt in zip(
                generation_outputs, data[start_idx:end_idx], prompts[start_idx:end_idx]
            ):
                response = generation_output.outputs[0].text.strip()
                is_no_answer = self.parse_reponse_verdict(response)
                output_obj = {
                    "context": d["context"],
                    "question": d["question"],
                    "answer": d["answer"],
                    "prompt": prompt,
                    "response": response,
                    "is_no_answer": is_no_answer,
                }
                output.append(output_obj)

            total_output.extend(output)
            if output_path:
                write_jsonl(output, output_path, mode="a", verbose=False)
            p_bar.update(end_idx - start_idx)
        p_bar.close()
        total_output = [d for d in total_output if not d["is_no_answer"]]
        return total_output

    def run(
        self,
        input_path,
        output_path="",
        n_examples=0,
        max_tokens=16,
        temperature=0,
        top_p=0,
        top_k=-1,
        batch_size=100,
        use_tqdm=False,
    ):
        data = self.get_data(input_path, n_examples)
        # data = self.filter_context_dependent(
        #     data,
        #     max_tokens=max_tokens,
        #     temperature=temperature,
        #     top_p=top_p,
        #     top_k=top_k,
        #     batch_size=batch_size,
        #     output_path="output/bioasq/filter_question_vllm/train_chunks_filter_context_dependent.jsonl",
        #     use_tqdm=use_tqdm,
        # )
        data = self.generate_answer(
            data,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            batch_size=batch_size,
            # output_path="output/bioasq/filter_question_vllm/train_chunks_answer.jsonl",
            use_tqdm=use_tqdm,
        )
        data = self.filter_no_answer(
            data,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            batch_size=batch_size,
            # output_path="output/bioasq/filter_question_vllm/train_chunks_filter_no_answer.jsonl",
            use_tqdm=use_tqdm,
        )
        return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model_path", type=str, default="")
    parser.add_argument("-i", "--input_path", type=str, required=True)
    parser.add_argument("-o", "--output_path", type=str, required=True)
    parser.add_argument("-n", "--n_examples", type=int, default=0)
    parser.add_argument("-b", "--batch_size", type=int, default=1000)
    parser.add_argument("-t", "--tensor_parallel_size", type=int, default=1)
    parser.add_argument("--example_path", type=str, help="path to fewfewshot examples")
    parser.add_argument("--max_tokens", type=int, default=16)
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--top_p", type=float, default=1.0)
    parser.add_argument("--top_k", type=int, default=50)
    args = parser.parse_args()

    # set up logger
    qa_generator = QuestionFilter(
        model_path=args.model_path, tensor_parallel_size=args.tensor_parallel_size
    )
    output = qa_generator.run(
        input_path=args.input_path,
        output_path="",
        n_examples=args.n_examples,
        max_tokens=args.max_tokens,
        temperature=args.temperature,
        top_p=args.top_p,
        top_k=args.top_k,
        batch_size=args.batch_size,
        use_tqdm=False,
    )
    prepare_file(args.output_path)

    logger.info("Convert to embedding finetuning data")

    idx = 0
    contexts = set([d["context"] for d in output])
    context_2_id = {c: idx for idx, c in enumerate(contexts)}

    dict_data = {}
    for d in output:
        context = d["context"]
        if context not in dict_data:
            dict_data[context] = {}
        question = d["question"]
        answer = d["answer"]
        dict_data[context][question] = answer

    output = []
    for k, v in dict_data.items():
        context = k
        for question, answer in v.items():
            output.append(
                {
                    "query": question,
                    "answer": answer,
                    "pos": [context],
                    "neg": [],
                }
            )
    write_jsonl(output, args.output_path)
    logger.info(f"{len(output)} CQA triplets")
    logger.info(f"Save data to {args.output_path}")
