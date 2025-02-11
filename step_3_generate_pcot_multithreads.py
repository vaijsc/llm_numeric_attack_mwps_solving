from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import json
import glob
import openai
import ast
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
        # openai.api_key = "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"
        openai.api_key = "sk-proj-dvhW7f2JAWx0ovDsb89nT3BlbkFJn1L7bv90yM0ypwiJpHfz"
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

def check_condition_and_result(text, ques_idx, line):        
    conditions = extract_conditions(text)
    parsed = ast.parse(text)

    variables_dict = {}
    local_vars = {}

    for idx, node in enumerate(parsed.body):
        if isinstance(node, ast.Assign):
            var_name = node.targets[0].id 
            var_value = eval_expr(node.value, local_vars)
            local_vars[var_name] = var_value
            variables_dict[var_name] = {
                "value": var_value, 
                "condition": conditions.get(var_name, {}),
                "idx": idx
            }
    
    result_key = None
    tmp_idx = -1
    for var, info in variables_dict.items():
        value = info['value']
        condition = info['condition']
        if not check_condition(value, condition, variables_dict):
            return False 
        if info['idx'] > tmp_idx:
            result_key = var 
            tmp_idx = info['idx']
    
    pred = variables_dict[result_key]['value']    
    pred = str(pred).replace('.00', '').replace('.0', '')

    ground_truth = line['ground_truth']
    return pred == ground_truth

def process_file(index):
    with open(f'results/gpt4omini/zero_shot_original/MATH/algebra_filtered/{index}.json') as fr:
        line = json.load(fr)
        prompt = TEXT + '\n\n' + TEMPLATE.format(question=line['problem'])
    
    with open(f'data/pcot/MATH/algebra/prompt/{index}.txt', 'w') as fw:
        fw.write(prompt)

    output = None
    count_try = 0
    while output is None and count_try < 5:
        try:
            output = get_response(prompt)[0]
            if check_condition_and_result(output.replace('//', '/'), index, line):
                with open(f'data/pcot/MATH/algebra/original_pcot/{index}.py', 'w') as fw:
                    fw.write(output)
                return True
            else:
                output = None
                count_try += 1
        except:
            count_try += 1
            output = None
    return False

def main():
    all_files = glob.glob('results/gpt4omini/zero_shot_original/MATH/algebra_filtered/*.json')
    input_ids = sorted(int(f.split('/')[-1][:-5]) for f in all_files)
    
    n_workers = 2  # Adjust based on your system capacity
    with ThreadPoolExecutor(max_workers=n_workers) as executor:
        futures = {executor.submit(process_file, idx): idx for idx in input_ids if idx > 1171}
        for future in tqdm(as_completed(futures), total=len(futures)):
            index = futures[future]
            try:
                result = future.result()
                if not result:
                    print(f"Processing failed for index {index}")
            except Exception as e:
                print(f"Error processing index {index}: {e}")

if __name__ == "__main__":
    main()
