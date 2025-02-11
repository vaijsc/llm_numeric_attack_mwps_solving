import json 
import glob 
def check_original_question(index, prefix):
    path = f"{prefix}/{index}.json" 
    with open(path) as fr:
        line = json.load(fr)
    return line["ground_truth"] == line["vllm_pred_answer"]

all_new_question_files = glob.glob(f"data/pcot/MATH/algebra/new_question/*.jsonl")
question_ids = [f.split("/")[-1][:-6] for f in all_new_question_files]
question_ids = sorted([int(id) for id in question_ids])

# model = 'THUDM/chatglm3-6b'.split('/')[-1]
# model = 'meta-math/MetaMath-Mistral-7B'.split('/')[-1]
model = 'meta-llama/Meta-Llama-3-8B-Instruct'.split('/')[-1]

path = f'results/{model}/MATH/algebra/zero_shot'
# if 'llama' in model.lower():
    # path+='_filtered'
count = 0
for i in question_ids:
    if check_original_question(i, path):
        count+=1

print('len question ids: ', len(question_ids))
print('count: ', count)
print('clean acc: ', count/len(question_ids))

count_attacked = 0
path_attacked_files = glob.glob(f'results/{model}/MATH/algebra/zero_shot_attacked_gemini_verified/*.json')
# if 'llama' in model.lower():
#     path_attacked_files = glob.glob(f'results/{model}/MATH/algebra/zero_shot_attacked_gemini_verified_v2/*.json')
path_attacked_ids = [f.split('/')[-1][:-5] for f in path_attacked_files]
path_attacked_ids = sorted([int(f) for f in path_attacked_ids])

for i in question_ids:
    if check_original_question(i, path) and i in path_attacked_ids:
        count_attacked+=1

print('num attacked: ', count_attacked)
print('num attack acc: ', (count-count_attacked)/450)
print('ASR: ', count_attacked/count)