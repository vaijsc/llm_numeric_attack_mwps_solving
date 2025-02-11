import glob 
import shutil
from tqdm import tqdm 
all_new_question_files = glob.glob(f"data/pcot/MATH/algebra/new_question/*.jsonl")
all_new_pcot_files = glob.glob(f"data/pcot/MATH/algebra/new_pcot/*.jsonl")
llama3_zero_shot_outputs = glob.glob(f"results/Meta-Llama-3-8B-Instruct/MATH/algebra/zero_shot/*.json")

question_ids = [f.split("/")[-1][:-6] for f in all_new_question_files]
pcot_ids = [f.split("/")[-1][:-6] for f in all_new_pcot_files]
llama3_zero_shot_ids = [f.split("/")[-1][:-5] for f in llama3_zero_shot_outputs]

question_ids = sorted([int(id) for id in question_ids])
pcot_ids = sorted([int(id) for id in pcot_ids])
llama3_zero_shot_ids = sorted([int(id) for id in llama3_zero_shot_ids])

for id in tqdm(question_ids):
    src_path = f"results/Meta-Llama-3-8B-Instruct/MATH/algebra/zero_shot/{id}.json"
    dst_path = f"results/Meta-Llama-3-8B-Instruct/MATH/algebra/zero_shot_filtered/{id}.json"

    shutil.copy(src_path, dst_path)