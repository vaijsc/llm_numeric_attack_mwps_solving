from vllm import LLM, SamplingParams
from utils import get_examples_gsm8k, GSMDataset, extract_answer, return_predicted_answer
from utils import extract_answer, return_predicted_answer, safety_settings
from utils import maybe_remove_comma, find_number
import re
import collections
import torch
from prompt_mistral import PROMPT, TEMPLATE, TEMPLATE_ZERO_SHOT
import glob 
ANS_RE = re.compile(r"#### (\-?[0-9\.\,]+)")
INVALID_ANS = "[invalid]"
PATTERN = r"(?:\(|\s)([A-Z])\.?(?:\)|\s|$)"
from tqdm import tqdm
import json 

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


from datasets import load_dataset 
ds = load_dataset("ChilleD/MultiArith", split = 'test')

vllm_model = LLM(model='THUDM/chatglm2-6b', dtype = torch.float16, trust_remote_code=True)

def llm_attack_zero_shot(question, model):
    q_prompt = TEMPLATE_ZERO_SHOT.format(question=question)
    responses  = get_response([q_prompt for _ in range(30)], model)
    ans =  [extract_answer_predict(response) for response in responses]
    counter = collections.Counter(ans[:30])
    pred_res = counter.most_common(1)[0][0]
    save_dict = {
        'q_prompt': q_prompt, 
        'response': responses,
        'ans': ans,
        'pred_res': pred_res
    }

    return save_dict 


# qids = glob.glob(f'data/pot_new_question_attack_by_llama3_8b_zero_shot/*.txt')
# qids = [qid.split('/')[-1][:-4] for qid in qids]
# qids = sorted([int(qid) for qid in qids])
################################## infer original, atatck question ###############################
qids_all = glob.glob(f'data/pot_generated_data_before_attack_final/*.json')
qids_all = [qid.split('/')[-1][:-5] for qid in qids_all]
qids_all = sorted([int(qid) for qid in qids_all])

for qid in tqdm(qids_all):
    old_question = ds[qid]['question']
    with open(f'results/chatglm2_6b_original_zero_shot/{qid}.json', 'w') as fw:
        json.dump(llm_attack_zero_shot(old_question, vllm_model), fw, indent = 4)