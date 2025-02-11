from tqdm import tqdm
from prompts import TEMPLATE, TEXT
from utils import extract_conditions, check_condition, eval_expr, safety_settings
import ast
from tqdm import tqdm 
import json 
import glob
import openai

class OpenAIModel:
    model_path: str
    engine: str = ""
    use_azure: bool = False
    timeout: int = 60
    temperature: float = 1

    def load(self):
        openai.api_key = "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"
        self.engine = "gpt-4o-mini"

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
                    temperature=1,
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


model = OpenAIModel()

def get_response(prompt):
    output = []
    while len(output) < 5:
        try:
            response = model.run(prompt=prompt)
            if response.replace('\n\n\n', '\n').replace('\n\n', '\n') not in output:
                output.append(response.replace('\n\n\n', '\n').replace('\n\n', '\n'))
        except:
            import time
            time.sleep(1)
    return output

def check_condition_and_result(text, ques_idx):        
        # extract conditions 
        conditions = extract_conditions(text)
        # parse the text to extract variable assignments
        parsed = ast.parse(text)

        variables_dict = {}
        local_vars = {}

        for idx, node in enumerate(parsed.body):
            if isinstance(node, ast.Assign):
                var_name = node.targets[0].id 
                var_value = eval_expr(node.value, local_vars)
                local_vars[var_name] = var_value
                variables_dict[var_name] = {
                    "value" : var_value, 
                    "condition": conditions.get(var_name, {}),
                    "idx": idx
                }
        
        result_key = None
        tmp_idx = -1
        for var, infor in variables_dict.items():
            value = infor['value']
            condition = infor['condition']
            if check_condition(value, condition, variables_dict) == False:
                # print(f'file {i} error in condition!!!')
                # error_condition_list.append(i)
                return False 
            if infor['idx'] > tmp_idx:
                result_key = var 
                tmp_idx = infor['idx']
        
        pred = variables_dict[result_key]['value']    
        pred = str(pred).replace('.00', '').replace('.0', '')
        # with open(f'pot_new_output_extract_answer/{i}.txt', 'w') as fw:
        #     fw.write(pred)

        ground_truth = line['ground_truth']

        if pred != ground_truth:
            # print(f'file {i} error in result!!!')
            # error_result_list.append(i)
            return False
        return True 

all_file = glob.glob(f'results/gpt4omini/zero_shot_original/MATH/algebra_filtered/*.json')
print(len(all_file))
input_ids = [int(f.split('/')[-1][:-5]) for f in all_file]
input_ids = list(sorted(input_ids))

for index in tqdm(input_ids):
    if index < 598:
        continue
    print('Index: ', index)
    with open(f'results/gpt4omini/zero_shot_original/MATH/algebra_filtered/{index}.json') as fr:
        line = json.load(fr)
        prompt = TEXT + '\n\n'+  TEMPLATE.format(question=line['problem'])

    with open(f'data/pcot/MATH/algebra/prompt/{index}.txt', 'w') as fw:
        fw.write(prompt)

    output = None
    count_try = 0
    while output == None and count_try < 5:
        try:
            output = get_response(prompt)[0]
            print('output:\n', output)
            with open('check_pcot.txt', 'w') as fw:
                fw.write(output)
            if check_condition_and_result(output.replace('//', '/'), index) == False:
                output = None
                count_try += 1
        except:
            count_try += 1
            output = None

    if output == None:
        continue
    else:
        with open(f'data/pcot/MATH/algebra/original_pcot/{index}.py', 'w') as fw:
            fw.write(output)