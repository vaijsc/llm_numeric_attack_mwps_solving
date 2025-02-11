import collections
import glob 
import json 
from tqdm import tqdm 
import ast
import re
import json 
from tqdm import tqdm
from utils import extract_conditions, eval_expr, check_condition, safety_settings
from prompt_change_question import PROMPT
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
from prompts_vllm import PROMPT, TEMPLATE, TEMPLATE_ZERO_SHOT
ANS_RE = re.compile(r"#### (\-?[0-9\.\,]+)")
INVALID_ANS = "[invalid]"
PATTERN = r"(?:\(|\s)([A-Z])\.?(?:\)|\s|$)"


os.environ['CUDA_VISIBLE_DEVICES']="2"


def check_condition_and_get_answer(pcot_answer):
    new_conditions = extract_conditions(pcot_answer)
    new_parsed = ast.parse(pcot_answer)
    new_variables_dict = {}
    new_local_vars = {}
    
    res = None
    tmp_idx = -1 
    for index, node in enumerate(new_parsed.body):
        if isinstance(node, ast.Assign):
            var_name = node.targets[0].id
            var_value = eval_expr(node.value, new_local_vars)
            new_local_vars[var_name] = var_value 
            new_variables_dict[var_name] = {
                "value": var_value,
                "condition": new_conditions.get(var_name, {}),
                "index": index
            }
            if index > tmp_idx:
                res = var_value
    # print('result: ', res)
    try:
        if res % 1 != 0:
            return (False, res)
    except:
        return (False, res)
    for new_var, new_infor in new_variables_dict.items():
        new_value = new_infor["value"]
        new_condition = new_infor["condition"]
        # if new_condition['direct_from_question'] == False and new_value == 0:
        #     return False
        if check_condition(new_value, new_condition, new_variables_dict) == False:
            return (False, res)
    return (True, res)


def check_original_question(index, prefix):
    path = f"{prefix}/{index}.json" 
    with open(path) as fr:
        line = json.load(fr)
    return line["ground_truth"] == line["vllm_pred_answer"]

all_new_question_files = glob.glob(f"data/pcot/MATH/algebra/new_question/*.jsonl")
question_ids = [f.split("/")[-1][:-6] for f in all_new_question_files]
question_ids = sorted([int(id) for id in question_ids])


model_name_or_path = "meta-math/MetaMath-Mistral-7B"
vllm_model = LLM(model=model_name_or_path, dtype = torch.float16)

def extract_answer_predict(response):
    short_responses = maybe_remove_comma(find_number(response))
    return short_responses

stop_tokens = ["\n\n###", "Question:", "Question", "USER:", "USER", "ASSISTANT:", "ASSISTANT", "Instruction:", "Instruction", "Response:", "Response"]
sampling_params = SamplingParams(temperature=1, top_p=1, max_tokens=512, stop=stop_tokens)


def get_response(prompt, model):
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

    responses = get_response(prompts, vllm_model)
    ans =  [extract_answer_predict(response) for response in responses]
    ans = [a.replace('.000', '').replace('.00', '').replace('.0', '') for a in ans]

    counter = collections.Counter(ans[:30])
    pred_res = counter.most_common(1)[0][0]

    example['vllm_responses'] = responses
    example['vllm_answers'] = ans 
    example['vllm_pred_answer'] = pred_res 
    return example 

path = 'results/MetaMath-Mistral-7B/MATH/algebra/zero_shot'
for id in tqdm(question_ids):
    if check_original_question(id, path):
        # 1. open new question 
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
        for i, (question, pcot_answer) in enumerate(tqdm(zip(questions, pcot_answers))):
            (_, res) = check_condition_and_get_answer(pcot_answer)
            example = {
                'index_adversarial_question': i,
                'problem': question, 
                'pcot_answer': pcot_answer,
                'answer': str(res).replace('.000', '').replace('.00', '').replace('.0', '')
            }
            new_example = inference_vllm_zero_shot(example, vllm_model)

            if new_example['vllm_pred_answer'] != new_example["answer"]:
                with open(f"results/{model_name_or_path.split('/')[-1]}/MATH/algebra/zero_shot_attacked/{id}.json", 'w') as fw:
                    json.dump(new_example, fw, indent = 4) 
                print(f'Attack in id={id} success.')
                break 