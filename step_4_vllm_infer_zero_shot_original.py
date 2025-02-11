import collections
import json 
from pprint import pprint
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


os.environ['CUDA_VISIBLE_DEVICES']="2"

model_name_or_path = "meta-llama/Meta-Llama-3-8B-Instruct"
vllm_model = LLM(model=model_name_or_path, dtype = torch.float16)
qids = glob.glob(f'results/gpt4omini/zero_shot_original/MATH/algebra_filtered/*.json')
qids = sorted([int(path.split('/')[-1][:-5]) for path in qids])

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


def inference_vllm_zero_shot(example, model):
    prompt = TEMPLATE_ZERO_SHOT.format(question=example['problem'])
    prompts = [prompt for _ in range(30)]

    responses = get_response(prompts, vllm_model)
    ans =  [extract_answer_predict(response) for response in responses]
    ans = [a.replace('.000', '').replace('.00', '').replace('.0', '') for a in ans]

    counter = collections.Counter(ans[:30])
    pred_res = counter.most_common(1)[0][0]

    example['vllm_responses'] = responses
    example['vllm_answers'] = ans 
    example['vllm_pred_answer'] = pred_res 
    
    return example 

os.makedirs(f"results/{model_name_or_path.split('/')[-1]}/MATH/algebra/zero_shot/")

for qid in tqdm(qids):
    print('qid = ', qid)
    with open(f'results/gpt4omini/zero_shot_original/MATH/algebra_filtered/{qid}.json', 'r') as fr:
        example = json.load(fr)
    new_example = inference_vllm_zero_shot(example, vllm_model)

    with open(f"results/{model_name_or_path.split('/')[-1]}/MATH/algebra/zero_shot/{qid}.json", 'w') as fw:
        json.dump(new_example, fw, indent = 4) 
    