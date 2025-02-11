import google.generativeai as genai
from utils import get_examples_gsm8k, GSMDataset, extract_answer, return_predicted_answer
from utils import extract_answer, return_predicted_answer, safety_settings
from utils import maybe_remove_comma, find_number
import re
import collections
import torch
import openai

PROMPT = """### Instruction: What is the degree of the polynomial ${{4 +5x^3 +100 +2\\pi x^4 + \\sqrt{{10}}x^4 +9}}$?
### Response: This polynomial is not written in standard form. However, we don't need to write it in standard form, nor do we need to pay attention to the coefficients. We just look for the exponents on $x$. We have an $x^4$ term and no other term of higher degree, so $\\boxed{{4}}$ is the degree of the polynomial.

### Instruction: {question}
### Response:"""


ANS_RE = re.compile(r"#### (\-?[0-9\.\,]+)")
INVALID_ANS = "[invalid]"
PATTERN = r"(?:\(|\s)([A-Z])\.?(?:\)|\s|$)"
from tqdm import tqdm
import json 

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
        self.engine = "gpt-3.5-turbo-0125"
        # self.engine = 'gpt-4o-mini'

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
                    temperature=1,  # this is the degree of randomness of the model's output
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
    # print('len prompt: ', len(prompt))
    while len(output) < 5:
        try:
            response = model.run(prompt = prompt)
            if response.replace('\n\n\n', '\n').replace('\n\n', '\n') not in output:
                output.append(response.replace('\n\n\n', '\n').replace('\n\n', '\n'))
        except:
            import time
            time.sleep(1)
    return output

from datasets import load_dataset
ds = load_dataset("lighteval/MATH", "algebra")['test']

def chatgpt_inference(example, model):
    q_prompt = PROMPT.format(question=example['problem'])
    responses  = get_response(q_prompt, model)
    ans =  [extract_answer_predict(response) for response in responses]
    counter = collections.Counter(ans[:30])
    pred_res = counter.most_common(1)[0][0]
    example['prompt'] = q_prompt
    example['responses'] = responses
    example['pred_answers'] = pred_res
    example['final_pred_answer'] = ans
    example['ground_truth'] = extract_answer_predict(example['solution'])
    return example


kwargs = {}
model = OpenAIModel(**kwargs)

for idx, example in enumerate(tqdm(ds)):
    with open(f'results/chatgpt/zero_shot_original/MATH/algebra/{idx}.json', 'w') as fw:
        json.dump(chatgpt_inference(example, model), fw, indent = 4)