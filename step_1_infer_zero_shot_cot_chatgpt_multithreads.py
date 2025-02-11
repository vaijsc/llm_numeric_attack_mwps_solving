import google.generativeai as genai
from utils import get_examples_gsm8k, GSMDataset, extract_answer, return_predicted_answer
from utils import extract_answer, return_predicted_answer, safety_settings
from utils import maybe_remove_comma, find_number
import re
import collections
import torch
import openai
from concurrent.futures import ThreadPoolExecutor
from datasets import load_dataset
import json
from tqdm import tqdm

# Set up constants and regex
PROMPT = """### Instruction: {question}
Let’s think step by step.
### Response:"""

ANS_RE = re.compile(r"#### (\-?[0-9\.\,]+)")
INVALID_ANS = "[invalid]"
PATTERN = r"(?:\(|\s)([A-Z])\.?(?:\)|\s|$)"

# Utility functions
def extract_answer_predict(response):
    short_responses = maybe_remove_comma(find_number(response))
    return short_responses

class OpenAIModel:
    model_path: str
    engine: str = ""
    use_azure: bool = False
    timeout: int = 60
    temperature: float = 1

    def load(self):
        openai.api_key = "sk-proj-dvhW7f2JAWx0ovDsb89nT3BlbkFJn1L7bv90yM0ypwiJpHfz"
        self.engine = "gpt-4o-mini"

    def run(self, prompt: str) -> str:
        self.load()
        output = ""
        error_message = "The response was filtered"

        while not output:
            try:
                key = "engine" if self.use_azure else "model"
                kwargs = {key: self.engine}
                response = openai.ChatCompletion.create(
                    messages=[{"role": "user", "content": prompt}],
                    timeout=self.timeout,
                    request_timeout=self.timeout,
                    temperature=1,
                    **kwargs,
                )
                if response.choices[0].finish_reason == "content_filter":
                    raise ValueError(error_message)
                output = response.choices[0].message.content
            except Exception as e:
                print(e)
                if error_message in str(e):
                    output = error_message

            if not output:
                print("OpenAIModel request failed, retrying.")

        return output


def get_response(prompt, gemini_model):
    output = []
    while len(output) < 5:
        try:
            response = model.run(prompt=prompt)
            if response.replace('\n\n\n', '\n').replace('\n\n', '\n') not in output:
                output.append(response.replace('\n\n\n', '\n').replace('\n\n', '\n'))
        except:
            import time
            time.sleep(1)
    return output

def chatgpt_inference(example, model):
    q_prompt = PROMPT.format(question=example['problem'])
    responses = get_response(q_prompt, model)
    ans = [extract_answer_predict(response) for response in responses]
    counter = collections.Counter(ans[:30])
    pred_res = counter.most_common(1)[0][0]
    example['prompt'] = q_prompt
    example['responses'] = responses
    example['pred_answers'] = pred_res
    example['final_pred_answer'] = ans
    example['ground_truth'] = extract_answer_predict(example['solution'])
    return example

# Initialize dataset and model
ds = load_dataset("lighteval/MATH", "algebra")['test']
model = OpenAIModel()

# Define function to process and save each example
def process_and_save(example, idx):
    result = chatgpt_inference(example, model)
    with open(f'results/gpt4omini/zero_shot_original/MATH/algebra/{idx}.json', 'w') as fw:
        json.dump(result, fw, indent=4)

# Set the number of workers
n_workers =  16 # Adjust based on your CPU cores or the level of parallelism desired

# Run inference with ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=n_workers) as executor:
    list(tqdm(executor.map(process_and_save, ds, range(len(ds))), total=len(ds)))
