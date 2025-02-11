import glob 
import google.generativeai as genai
from utils import get_examples_gsm8k, GSMDataset, extract_answer, return_predicted_answer, safety_settings
from utils import maybe_remove_comma, find_number
import re
import collections
import torch
from tqdm import tqdm
import json
from datasets import load_dataset
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import collections
import glob 
import json 
from tqdm import tqdm 
import ast
import re
import json 
from tqdm import tqdm
from utils import extract_conditions, eval_expr, check_condition, safety_settings
import pickle 
from vllm import LLM, SamplingParams
import torch 
from transformers import AutoTokenizer
import glob 
from vllm import LLM
import torch 
from tqdm import tqdm
import glob
from prompts_vllm import TEMPLATE_ZERO_SHOT
from utils import get_examples_gsm8k, GSMDataset, extract_answer, return_predicted_answer
from utils import extract_answer, return_predicted_answer, safety_settings
from utils import maybe_remove_comma, find_number
import os 
import re 
from vllm import LLM, SamplingParams
from prompts_vllm import TEMPLATE, TEMPLATE_ZERO_SHOT
ANS_RE = re.compile(r"#### (\-?[0-9\.\,]+)")
INVALID_ANS = "[invalid]"
PATTERN = r"(?:\(|\s)([A-Z])\.?(?:\)|\s|$)"


os.environ['CUDA_VISIBLE_DEVICES']="1"

all_attacked_file = glob.glob(f"results/chatglm3-6b/MATH/algebra/zero_shot_attacked/*.json")
all_attacked_ids = [f.split('/')[-1][:-5] for f in all_attacked_file]
all_attacked_ids = sorted([int(f) for f in all_attacked_ids])
######################### 1. function infer = gemini SC###################################
# Define constants and configurations
PROMPT = """### Instruction: {question}
Let’s think step by step. If not have answer return "not exist" and put final result in the end, if final result is fraction, please convert it to float.
### Response:"""
ANS_RE = re.compile(r"#### (\-?[0-9\.\,]+)")
INVALID_ANS = "[invalid]"
PATTERN = r"(?:\(|\s)([A-Z])\.?(?:\)|\s|$)"

# GOOGLE_API_KEY = "AIzaSyBLaB5zJKfZTcMD2FgTWRVc2oM0s2lb8YI"  # Insert your API key here
# genai.configure(api_key=GOOGLE_API_KEY)
# gemini_model = genai.GenerativeModel('gemini-1.5-flash', safety_settings=safety_settings)
# print('Gemini model: ', gemini_model)

from openai_model import OpenAIModel
gpt_model = OpenAIModel()


# Function to process each example
def extract_answer_predict(response):
    if "not exist" in response.lower():
        return "-10000"
    short_responses = maybe_remove_comma(find_number(response))
    return short_responses

def get_response(prompt, model):
    output = []
    while len(output) < 3:
        response = model.run(prompt)
        if response.replace('\n\n\n', '\n').replace('\n\n', '\n') not in output:
            output.append(response.replace('\n\n\n', '\n').replace('\n\n', '\n'))
    return output

def gemini_generate_answer(example):
    q_prompt = PROMPT.format(question=example['problem'])
    responses = get_response(q_prompt, gpt_model)
    ans = [extract_answer_predict(response) for response in responses]
    counter = collections.Counter(ans[:15])
    pred_res = counter.most_common(1)[0][0]
    example['gemini_responses'] = responses
    example['gemini_pred_answers'] = ans
    example['gemini_final_pred_answer'] = pred_res
    example['gemini_frequent_pred_answer'] = counter.most_common(1)[0][1]
    return example

################################# 2. function infer = vllm #############################
model_name_or_path = "THUDM/chatglm3-6b"
vllm_model = LLM(model=model_name_or_path, dtype = torch.float16, trust_remote_code=True)
stop_tokens = ["\n\n###", "Question:", "Question", "USER:", "USER", "ASSISTANT:", "ASSISTANT", "Instruction:", "Instruction", "Response:", "Response"]
sampling_params = SamplingParams(temperature=1, top_p=1, max_tokens=512, stop=stop_tokens)

def get_response_vllm(prompt, model):
    output = []
    while len(output) < len(prompt):
        responses = model.generate(prompt, sampling_params, use_tqdm=False)
        for i in range(len(responses)):
            if responses[i].outputs[0].text.replace('\n\n\n', '\n').replace('\n\n', '\n') not in output:
                output.append(responses[i].outputs[0].text.replace('\n\n\n', '\n').replace('\n\n', '\n'))
    return output

def inference_vllm_zero_shot(example, model):
    prompt = TEMPLATE_ZERO_SHOT.format(question=example['problem'])
    prompts = [prompt for _ in range(15)]

    responses = get_response_vllm(prompts, vllm_model)
    ans =  [extract_answer_predict(response) for response in responses]
    ans = [a.replace('.000', '').replace('.00', '').replace('.0', '') for a in ans]

    counter = collections.Counter(ans[:15])
    pred_res = counter.most_common(1)[0][0]

    example['vllm_responses'] = responses
    example['vllm_answers'] = ans 
    example['vllm_pred_answer'] = pred_res 
    return example 


def use_attacked_sample_llama3(llama3_prefix_file_attacked, id):
    if os.path.exists(f"{llama3_prefix_file_attacked}/{id}.json"):
        with open(f"{llama3_prefix_file_attacked}/{id}.json") as fr:
            llama_example = json.load(fr)
        
        llama_example = inference_vllm_zero_shot(llama_example, vllm_model)

        if llama_example['vllm_pred_answer'] != llama_example["gemini_final_pred_answer"] and llama_example["gemini_final_pred_answer"]!="-10000":
            with open(f"results/{model_name_or_path.split('/')[-1]}/MATH/algebra/zero_shot_attacked_gemini_verified/{id}.json", 'w') as fw:
                json.dump(llama_example, fw, indent = 4) 
            print(f'Attack in id={id} success in case 2.')
        return True
    else:
        return False

################################main####################################
for id in tqdm(all_attacked_ids):
    # if id > 733:
        with open(f"results/chatglm3-6b/MATH/algebra/zero_shot_attacked/{id}.json") as fr:
            attacked_example = json.load(fr)
        attacked_example = gemini_generate_answer(attacked_example)
        # if example["gemini_final_pred_answer"] == example["answer"]:
        if attacked_example['answer'] == attacked_example["gemini_final_pred_answer"] and attacked_example["gemini_final_pred_answer"]!="-10000" and attacked_example['gemini_frequent_pred_answer'] > 1:
            with open(f"results/{model_name_or_path.split('/')[-1]}/MATH/algebra/zero_shot_attacked_gemini_verified/{id}.json", 'w') as fw:
                json.dump(attacked_example, fw, indent = 4)
            print(f"Attack id={id} success in case 1.")
            
        else:
            # 1, open file attacked llama3:
            llama3_prefix_file_attacked = 'results/Meta-Llama-3-8B-Instruct/MATH/algebra/zero_shot_attacked_gemini_verified'
            # with open(f"{llama3_prefix_file_attacked}/{id}.json") as fr:
            #     llama_example = json.load(fr)
            
            # llama_example = inference_vllm_zero_shot(llama_example, vllm_model)

            # if llama_example['vllm_pred_answer'] != llama_example["gemini_final_pred_answer"] and llama_example["gemini_final_pred_answer"]!="-10000" and llama_example['gemini_frequent_pred_answer'] > 1:
            #     with open(f"results/{model_name_or_path.split('/')[-1]}/MATH/algebra/zero_shot_attacked_gemini_verified/{id}.json", 'w') as fw:
            #         json.dump(new_example, fw, indent = 4) 
            #     print(f'Attack in id={id} success in case 2.')
            if use_attacked_sample_llama3(llama3_prefix_file_attacked, id):
                continue
            else:
                questions = []
                with open(f"data/pcot/MATH/algebra/new_question/{id}.jsonl") as fr:
                    for line in fr:
                        questions.append(json.loads(line))
                
                # 2. open new pcot 
                pcot_answers = []
                with open(f"data/pcot/MATH/algebra/new_pcot/{id}.jsonl") as fr:
                    for line in fr:
                        pcot_answers.append(json.loads(line))
                
                assert len(questions) == len(pcot_answers)
                # 3. for zip attack  
                for i, (question, pcot_answer) in tqdm(enumerate(zip(questions, pcot_answers))):
                    if i <= attacked_example["index_adversarial_question"]:
                        continue
                    example = {
                        'index_adversarial_question': i,
                        'problem': question, 
                        'pcot_answer': pcot_answer,
                    }
                    example = gemini_generate_answer(example)
                    new_example = inference_vllm_zero_shot(example, vllm_model)

                    if new_example['vllm_pred_answer'] != new_example["gemini_final_pred_answer"] and new_example["gemini_final_pred_answer"]!="-10000" and new_example['gemini_frequent_pred_answer'] > 1:
                        with open(f"results/{model_name_or_path.split('/')[-1]}/MATH/algebra/zero_shot_attacked_gemini_verified/{id}.json", 'w') as fw:
                            json.dump(new_example, fw, indent = 4) 
                        print(f'Attack in id={id} success case 3.')
                        break 