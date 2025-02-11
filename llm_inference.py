from vllm import LLM, SamplingParams
from utils import get_examples_gsm8k, GSMDataset, extract_answer, return_predicted_answer
from utils import extract_answer, return_predicted_answer, safety_settings
from utils import maybe_remove_comma, find_number
import re
import collections
import torch
import json 

from prompts_vllm import PROMPT, TEMPLATE, TEMPLATE_ZERO_SHOT
ANS_RE = re.compile(r"#### (\-?[0-9\.\,]+)")
INVALID_ANS = "[invalid]"
PATTERN = r"(?:\(|\s)([A-Z])\.?(?:\)|\s|$)"


def extract_answer_predict(response):
    short_responses = maybe_remove_comma(find_number(response))
    return short_responses

stop_tokens = ["\n\n###", "Question:", "Question", "USER:", "USER", "ASSISTANT:", "ASSISTANT", "Instruction:", "Instruction", "Response:", "Response"]
sampling_params = SamplingParams(temperature=1, top_p=1, max_tokens=512, stop=stop_tokens)


def get_response(prompt, model):
    output = []
    while len(output) < len(prompt):
        responses = model.generate(prompt, sampling_params)
        for i in range(len(responses)):
            if responses[i].outputs[0].text.replace('\n\n\n', '\n').replace('\n\n', '\n') not in output:
                output.append(responses[i].outputs[0].text.replace('\n\n\n', '\n').replace('\n\n', '\n'))
    return output

def llm_attack(question, ground_truth, model, save_path):
    print('question: ', question)
    print('ground_truth:', ground_truth)
    q_prompt = (PROMPT + '\n' + TEMPLATE.format(question=question))
    responses  = get_response([q_prompt for _ in range(30)], model)
    ans =  [extract_answer_predict(response) for response in responses]
    ans = [a.replace('.0', '') for a in ans]
    print(ans)
    counter = collections.Counter(ans[:30])
    pred_res = counter.most_common(1)[0][0]
    print('pred_res == ground_truth: ', pred_res == str(int(ground_truth)))
    if pred_res == str(int(ground_truth)):
        return True
    else:
        save_dict = {
            'q_prompt': q_prompt, 
            'response': responses,
            'ans': ans,
            'pred_res': pred_res, 
            'ground_truth': ground_truth,
            'new_question': question
        }
        with open(save_path, 'w') as fw:
            json.dump(save_dict, fw, indent =4)
        return False

def llm_attack_zero_shot(question, ground_truth, model, save_path):
    print('question: ', question)
    print('ground_truth:', ground_truth)
    q_prompt = TEMPLATE_ZERO_SHOT.format(question=question)
    responses  = get_response([q_prompt for _ in range(30)], model)
    ans =  [extract_answer_predict(response) for response in responses]
    ans = [a.replace('.000', '').replace('.00', '').replace('.0', '') for a in ans]
    print(ans)
    counter = collections.Counter(ans[:30])
    pred_res = counter.most_common(1)[0][0]
    print('pred_res == ground_truth: ', pred_res == str(ground_truth))
    if pred_res == str(ground_truth):
        return True
    else:
        save_dict = {
            'q_prompt': q_prompt, 
            'response': responses,
            'ans': ans,
            'pred_res': pred_res, 
            'ground_truth': ground_truth,
            'new_question': question
        }
        with open(save_path, 'w') as fw:
            json.dump(save_dict, fw, indent =4)
        return False