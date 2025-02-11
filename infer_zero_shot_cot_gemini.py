import google.generativeai as genai
from utils import get_examples_gsm8k, GSMDataset, extract_answer, return_predicted_answer
from utils import extract_answer, return_predicted_answer, safety_settings
from utils import maybe_remove_comma, find_number
import re
import collections
import torch

PROMPT = """### Instruction: {question}
Let’s think step by step.
### Response:"""

ANS_RE = re.compile(r"#### (\-?[0-9\.\,]+)")
INVALID_ANS = "[invalid]"
PATTERN = r"(?:\(|\s)([A-Z])\.?(?:\)|\s|$)"
from tqdm import tqdm
import json 

def extract_answer_predict(response):
    short_responses = maybe_remove_comma(find_number(response))
    return short_responses


#########################################
GOOGLE_API_KEY="AIzaSyBLaB5zJKfZTcMD2FgTWRVc2oM0s2lb8YI"
genai.configure(api_key=GOOGLE_API_KEY)
gemini_model = genai.GenerativeModel('gemini-1.5-flash', safety_settings = safety_settings)
print('Gemini model: ', gemini_model)
##########################################
# def get_response(prompt, model):
#     response = model.generate_content(prompt)
#     return response.text


def get_response(prompt, gemini_model):
    output = []
    # print('len prompt: ', len(prompt))
    while len(output) < 5:
        # try:
            response = gemini_model.generate_content(prompt)
            if response.text.replace('\n\n\n', '\n').replace('\n\n', '\n') not in output:
                output.append(response.text.replace('\n\n\n', '\n').replace('\n\n', '\n'))
        # except:
            # import time
            # time.sleep(1)
    return output

from datasets import load_dataset
ds = load_dataset("lighteval/MATH", "counting_and_probability")['test']

def gemini_inference(example, model):
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




for idx, example in enumerate(tqdm(ds)):
    with open(f'results/gemini/zero_shot_original/MATH/counting_and_probability/{idx}.json', 'w') as fw:
        json.dump(gemini_inference(example, gemini_model), fw, indent = 4)