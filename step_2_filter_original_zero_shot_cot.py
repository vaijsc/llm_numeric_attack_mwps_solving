from collections import Counter
import glob 
import json 
from tqdm import tqdm 


all_file = glob.glob(f'results/gpt4omini/zero_shot_original/MATH/algebra/*.json')
input_ids = [int(f.split('/')[-1][:-5]) for f in all_file]
input_ids = list(sorted(input_ids))

for i in range(0, 1187):
    if i not in input_ids:
        print(i)

# print(input_ids)
print(len(all_file))

def Most_Common(lst):
    data = Counter(lst)
    print(data)
    return data.most_common(1)[0][0], data.most_common(1)[0][1]

count = 0
for i in tqdm(range(0, 1187)):
    with open(f'results/gpt4omini/zero_shot_original/MATH/algebra/{i}.json') as fr:
        line = json.load(fr)

    element_most_common, num_apperances = Most_Common(line['final_pred_answer'])

    if element_most_common == line['ground_truth'] and num_apperances >= 4:
        with open(f'results/gpt4omini/zero_shot_original/MATH/algebra_filtered/{i}.json', 'w') as fw:
            json.dump(
                line, fw, indent = 4
            )
        count += 1
print('Number examples after filtered: ', count)
