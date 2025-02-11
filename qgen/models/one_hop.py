import logging
from concurrent.futures import ThreadPoolExecutor
import re
from AutoRAG.qgen.models.gemini import Gemini
from AutoRAG.qgen.models.gpt import GPT
from vllm import LLM, SamplingParams
from tqdm import tqdm
from AutoRAG.qgen.utils import write_jsonl


logger = logging.getLogger(__name__)


class OneHopQAGenerator:
    model_type = ""
    model = None

    def parse_question_answer(self, text: str) -> list[dict]:
        qas = []
        match = re.search(
            r"\<question\>(?P<question>[^<]+)\</question\>\s+\<answer\>(?P<answer>[^<]+)\</answer\>",
            text,
        )
        if match:
            qas.append({
                "question": match.group("question").strip(),
                "answer": match.group("answer").strip(),
            })

        return qas

    def create_prompt(self, text, prompt_template):
        return prompt_template.format(context=text).strip()

    def create_messages(self, text, prompt_template, system_prompt=None):
        prompt = self.create_prompt(text, prompt_template)
        messages = []
        if system_prompt:
            messages = [{"role": "system", "content": system_prompt}]
        messages.append({"role": "user", "content": prompt})
        return messages

    def create_extended_messages(messages, previous_response):
        messages.extend(
            [
                {"role": "assistant", "content": previous_response},
                {"role": "user", "content": "Generate more questions and answers"},
            ]
        )
        return messages


class OneHopQAGeneratorGemini(OneHopQAGenerator):
    model_type = "gemini"

    def __init__(self, model_name, **kwargs):
        self.model = Gemini(model_name, **kwargs)

    def generate(
        self,
        prompt,
        sampling_params: dict = {},
        return_prompt=False,
        return_response=False,
    ) -> dict:
        response = self.model.generate(prompt=prompt, **sampling_params)
        output = {"qas": self.parse_question_answer(response)}

        if return_prompt:
            output["prompt"] = prompt
        if return_response:
            output["response"] = response

        return output

    def process_example(
        self,
        example,
        prompt_template,
        sampling_params,
        return_prompt=False,
        return_response=False,
    ) -> dict:
        prompt = self.create_prompt(example, prompt_template)
        output = self.generate(
            prompt,
            sampling_params=sampling_params,
            return_response=False,
            return_prompt=False,
        )
        # logger.info(f"Text: {chunk['text']}")
        # for qa in chunk['qas']:
        # logger.infof"Question: {qa['question']} | Answer: {qa['answer']}")
        output['text'] = example
        return output

    def process(
        self,
        data,
        prompt_template,
        n_workers,
        sampling_params,
        output_path,
        batch_size,
        return_prompt=False,
        return_response=False,
    ):
        with ThreadPoolExecutor(max_workers=n_workers) as executor:
            p_bar = tqdm(total=len(data), desc="examples", ncols=0)
            for start_idx in range(0, len(data), batch_size):
                end_idx = min(len(data), start_idx + batch_size)
                batch_result = tqdm(
                    executor.map(
                        lambda example: self.process_example(
                            example,
                            prompt_template=prompt_template,
                            sampling_params=sampling_params,
                            return_prompt=return_prompt,
                            return_response=return_response,
                        ),
                        data[start_idx:end_idx],
                    ),
                    total=len(data),
                    initial=start_idx + 1,
                    desc="batch_examples",
                    ncols=0,
                )
                write_jsonl(batch_result, output_path, mode="a", verbose=False)
                p_bar.update(end_idx - start_idx)


class OneHopQAGeneratorGPT(OneHopQAGenerator):
    model_type = "gpt"

    def __init__(self, model_name, **kwargs):
        self.model = GPT(model_name, **kwargs)

    def generate(
        self,
        messages,
        sampling_params: dict = {},
        return_prompt=False,
        return_response=False,
        return_messages=False,
    ) -> dict:
        response = self.model.generate(messages=messages, **sampling_params)
        output = {"qas": self.parse_question_answer(response)}

        if return_response:
            output["response"] = response
        if return_messages:
            output["messages"] = messages

        return output

    def process_example(
        self,
        example,
        prompt_template,
        sampling_params,
        return_messages=False,
        return_response=False,
    ) -> dict:
        prompt = self.create_messages(example, prompt_template)
        output = self.generate(
            prompt,
            sampling_params=sampling_params,
            return_response=False,
            return_prompt=False,
        )
        output['text'] = example
        return output

    def process(
        self,
        data,
        prompt_template,
        n_workers,
        sampling_params,
        output_path,
        batch_size,
        return_messages=False,
        return_response=False,
    ):
        with ThreadPoolExecutor(max_workers=n_workers) as executor:
            p_bar = tqdm(total=len(data), desc="examples", ncols=0)
            for start_idx in range(0, len(data), batch_size):
                end_idx = min(len(data), start_idx + batch_size)
                batch_result = tqdm(
                    executor.map(
                        lambda example: self.process_example(
                            example,
                            prompt_template,
                            sampling_params,
                            return_messages,
                            return_response,
                        ),
                        data[start_idx:end_idx],
                    ),
                    total=len(data),
                    initial=start_idx + 1,
                    desc="batch_examples",
                    ncols=0,
                )
                write_jsonl(batch_result, output_path, mode="a", verbose=False)
                p_bar.update(end_idx - start_idx)


class OneHopQAGeneratorVLLM(OneHopQAGenerator):
    model_type = "vllm"

    def __init__(self, model_name, **kwargs):
        self.model = LLM(model_name, **kwargs)

    def generate(
        self,
        messages: list[dict],
        sampling_params: dict = {},
        return_prompt=False,
        return_response=False,
        return_messages=False,
    ) -> dict:
        tokenizer = self.model.get_tokenizer()
        prompt = tokenizer.apply_chat_template(
            messages, add_generation_prompt=True, tokenize=False
        )
        response = self.model.generate(
            [prompt], sampling_params=sampling_params, use_tqdm=False
        )
        response = response[0].outputs[0].text.strip()
        output = {"qas": self.parse_question_answer(response)}

        if return_response:
            output["response"] = response
        if return_messages:
            output["messages"] = messages
        return output

    def batch_generate(
        self,
        messages_list: list[list[str]],
        sampling_params: dict = {},
        return_prompt=False,
        return_response=False,
        return_messages=False,
    ) -> dict:
        tokenizer = self.model.get_tokenizer()
        prompts = [
            tokenizer.apply_chat_template(
                messages, add_generation_prompt=True, tokenize=False
            )
            for messages in messages_list
        ]
        generation_outputs = self.model.generate(prompts, sampling_params)
        outputs = []
        for generation_output, messages in zip(generation_outputs, messages_list):
            response = generation_output.outputs[0].text.strip()
            output_obj = {"qas": self.parse_question_answer(response)}
            if return_response:
                output_obj["response"] = response
            if return_messages:
                output_obj["messages"] = messages
            outputs.append(output_obj)
        return outputs

    def process(
        self,
        data,
        prompt_template,
        sampling_params,
        output_path,
        batch_size,
        return_messages=False,
        return_response=False,
    ):
        messages_list = [
            self.create_messages(example, prompt_template) for example in data
        ]
        sampling_params = SamplingParams(**sampling_params)
        p_bar = tqdm(total=len(data), desc="examples", ncols=0)
        for start_idx in range(0, len(data), batch_size):
            end_idx = min(len(data), start_idx + batch_size)
            results = self.batch_generate(
                messages_list[start_idx:end_idx],
                sampling_params,
                return_messages=return_messages,
                return_response=return_response,
            )
            output = []
            for result, example in zip(results, data[start_idx:end_idx]):
                result['text'] = example
                output.append(result)
            write_jsonl(output, output_path, mode="a", verbose=False)
            p_bar.update(end_idx - start_idx)
        p_bar.close()
