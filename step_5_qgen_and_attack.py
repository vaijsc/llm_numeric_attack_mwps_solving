
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

all_file_original_py = glob.glob(f"data/pcot/MATH/algebra/original_pcot/*.py")
print("number file original pcot: ", len(all_file_original_py))
ids = [f.split('/')[-1][:-3] for f in all_file_original_py]
ids = sorted([int(id) for id in ids])


tokenizer = AutoTokenizer.from_pretrained('meta-llama/Meta-Llama-3-8B-Instruct')
vllm_model = LLM(model='meta-llama/Meta-Llama-3-8B-Instruct', dtype = torch.float16)

dataset = []
for i in range(max(ids)+1):
    if i in ids:
        with open(f'results/Meta-Llama-3-8B-Instruct/MATH/algebra/zero_shot/{i}.json') as fr:
            dataset.append(json.load(fr))
    else:
        dataset.append('_')

def parse_reponse(response: str):
    output = []
    # print('response: ', response)
    match = re.findall( r"\<question\>(?P<question>[^<]+)\</question\>", response)
    # print('match: ', match[0])
    for m in match:
        output.append(m)
    return output

def parse_reponse_2(response: str):
    # print('response: ', response)
    find_idx = response.find("\<question\>")
    output = response[find_idx + len("\<question\>"):]
    return output
def get_response(prompt, model):
    message = [
        {"role": "system", "content": "You are a chat bot that always follows instructions, and always gives short, concise answers."},
        {"role": "user", "content": prompt}
    ]
    
    message = tokenizer.apply_chat_template(
        message, add_generation_prompt=True, tokenize=False
    )

    sampling_params = {
        "max_tokens": 256,
        "temperature": 0.1,
        "top_p": 1.0,
        "stop": ['<|end_of_text|>', '<|eot_id|>']
    }
    sampling_params = SamplingParams(**sampling_params)
    
    response = ''
    while len(response) == 0:
        try:
            generation_output = model.generate(message, sampling_params)[0].outputs[0].text
            # print('output llm: ', generation_output)
            response = parse_reponse(generation_output)
            if len(response) >= 1:
                response = response[0]
            else:
                response = parse_reponse_2(generation_output)
                response = response
        except:
            response = ''
    return response

def gemini_generate_new_question(index, text, var, new_text, new_value, model):
    prompt = PROMPT.format(
        question = dataset[index]['problem'],
        answer = text,
        var_name = var, 
        new_value = new_value,
        new_answer = new_text
    )
    # print('PROMPT: \n', prompt)
    new_question = None
    while new_question == None:
        # try
            # print('---------------------------------------')
            # print('Original question: ', dataset[index]['problem'])
            new_question = get_response(prompt, model)
            new_question = new_question.replace('\nAnswer:', '')
            # if len(new_question.split(" ")) != len(dataset[index]['problem'].split(' ')) or new_question == dataset[index]['problem']:
            #     print('error in here')
            #     new_question = None
        # except:
            # new_question = None
    return new_question

# Extract conditions
def verify_condition_new_text(new_text):
    new_conditions = extract_conditions(new_text)
    new_parsed = ast.parse(new_text)
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

def change_one_value(text, variables_dict, index):
    new_question_list, new_pcot_answer_list = [], []
    for var, info in variables_dict.items():
        value = info["value"]
        condition = info["condition"]
        if condition['direct_from_question'] == True and condition['science_constant'] == False:
            print('value = ', value)
            # case 5: 5 chu so int:
            if value % 1 == 0 and value // 100000 == 0 and value // 10000 > 0:
            # if value % 1 == 0 and value // 10000 == 0 and value // 1000 > 0:

                print('vo case 5')
                tmp = 1000
                while tmp <= 100000 and (value + tmp) // 100000 == 0: 
                    if var + " = " + str(value) in text:
                        new_value = value + tmp
                        new_text = text.replace(var + " = " + str(value), var + " = " + str(new_value))
                        (is_satisfy_condition, res) = verify_condition_new_text(new_text)
                        if is_satisfy_condition:
                            new_question = gemini_generate_new_question(index, text, var, new_text, new_value, vllm_model)
                            new_question_list.append(new_question)
                            new_pcot_answer_list.append(new_text)
                            # print(new_question)
                            # if llm_attack(new_question, res, vllm_model) == False:
                                # return (new_text, var, new_value, res, new_question)
                    tmp += 1000

            # case 4: 4 chu so int:
            if value % 1 == 0 and value // 10000 == 0 and value // 1000 > 0:
                print('vo case 4')
                tmp = 100
                while tmp <= 10000 and (value + tmp) // 10000 == 0: 
                    if var + " = " + str(value) in text:
                        new_value = value + tmp
                        new_text = text.replace(var + " = " + str(value), var + " = " + str(new_value))
                        (is_satisfy_condition, res) = verify_condition_new_text(new_text)
                        if is_satisfy_condition:
                            new_question = gemini_generate_new_question(index, text, var, new_text, new_value, vllm_model)
                            new_question_list.append(new_question)
                            new_pcot_answer_list.append(new_text)                            
                            # if llm_attack(new_question, res, vllm_model) == False:
                            #     return (new_text, var, new_value, res, new_question)
                    tmp += 100

            # case 3: 3 chu so int:

            if value % 1 == 0 and value // 1000 == 0 and value // 100 > 0:
                print('vo case 3')
                tmp = 100
                while tmp <= 1000 and (value + tmp) // 1000 == 0: 
                    if var + " = " + str(value) in text:
                        new_value = value + tmp
                        new_text = text.replace(var + " = " + str(value), var + " = " + str(new_value))
                        (is_satisfy_condition, res) = verify_condition_new_text(new_text)
                        if is_satisfy_condition:
                            new_question = gemini_generate_new_question(index, text, var, new_text, new_value, vllm_model)
                            new_question_list.append(new_question)
                            new_pcot_answer_list.append(new_text)                            
                            # if llm_attack(new_question, res, vllm_model) == False:
                            # return (new_text, var, new_value, res, new_question)
                    tmp += 100

            # case 2: 2 chu so int:
            if value % 1 == 0 and value // 100 == 0 and value // 10 > 0:
                print('vo case 2')
                tmp = 10
                while tmp <= 100 and (value + tmp) // 100 == 0: 
                    if var + " = " + str(value) in text:
                        new_value = value + tmp
                        new_text = text.replace(var + " = " + str(value), var + " = " + str(new_value))
                        (is_satisfy_condition, res) = verify_condition_new_text(new_text)
                        if is_satisfy_condition:
                            new_question = gemini_generate_new_question(index, text, var, new_text, new_value, vllm_model)
                            new_question_list.append(new_question)
                            new_pcot_answer_list.append(new_text)    
                            # if llm_attack(new_question, res, vllm_model) == False:
                            # return (new_text, var, new_value, res, new_question)
                    tmp += 10

            # case 1: 1 chu so, int
            if value % 1 == 0 and value // 10 == 0:
                print('vo case 1')
                tmp = 1
                while tmp <= 10 and (value + tmp) // 10 == 0:
                    # try:
                        new_value = value + tmp
                        if var + " = " + str(value) in text:
                            new_text = text.replace(var + " = " + str(value), var + " = " + str(new_value))
                            # print('new text: ', new_text)
                            (is_satisfy_condition, res) = verify_condition_new_text(new_text)
                            if is_satisfy_condition:
                                new_question = gemini_generate_new_question(index, text, var, new_text, new_value, vllm_model)
                                new_question_list.append(new_question)
                                new_pcot_answer_list.append(new_text)                            
                                # if llm_attack(new_question, res, vllm_model) == False:
                                # return (new_text, var, new_value, res, new_question)
                        tmp += 1
                    # except:
                    #     tmp += 1

            if value % 1 == 0 and value // 10 == -1:
                print('vo case -1')
                tmp = 9
                while tmp > -10 and ((value + tmp) // 10 == -1 or (value + tmp) // 10 == 0):
                    try:
                        new_value = value + tmp
                        # print('new value:', new_value)
                        if var + " = " + str(value) in text:
                            new_text = text.replace(var + " = " + str(value), var + " = " + str(new_value))
                            # print('new text: ', new_text)
                            (is_satisfy_condition, res) = verify_condition_new_text(new_text)
                            if is_satisfy_condition:
                                new_question = gemini_generate_new_question(index, text, var, new_text, new_value, vllm_model)
                                new_question_list.append(new_question)
                                new_pcot_answer_list.append(new_text)                            
                                # if llm_attack(new_question, res, vllm_model) == False:
                                # return (new_text, var, new_value, res, new_question)
                        tmp -= 1
                    except:
                        tmp -= 1
            # case 6: >0 & <1 and (value/0.1)%1 == 0
            if value > 0 and value < 1 and (value/0.1)%1==0:
                print('vo case 0.1')
                tmp = 0.05 
                while tmp < 1 and (value + tmp) > 0 and (value + tmp) < 1:
                    new_value = value + tmp
                    start = text.find(var + " = ")
                    for j in range(start, len(text)):
                        if text[j:j+4] == " ###":
                            end = j
                            break
                    if text[start:end] in text:
                        new_text = text.replace(text[start:end], var + " = " + str(new_value))
                        (is_satisfy_condition, res) = verify_condition_new_text(new_text)
                        if is_satisfy_condition:
                            new_question = gemini_generate_new_question(index, text, var, new_text, new_value, vllm_model)
                            new_question_list.append(new_question)
                            new_pcot_answer_list.append(new_text)                            
                            # if llm_attack(new_question, res, vllm_model) == False:
                            # return (new_text, var, new_value, res, new_question)
                    tmp += 0.1
            # case 7
            # if value > 0 and value < 1 and (value/0.1)%1!=0 and (value/0.05)%1==0:
            #     tmp = 0.05
            #     while tmp < 1 and (value + tmp) > 0 and (value + tmp) < 1:
            #         new_value = value + tmp
            #         start = text.find(var + " = ")
            #         for j in range(start, len(text)):
            #             if text[j:j+4] == " ###":
            #                 end = j
            #                 break
            #         if text[start:end] in text:
            #             new_text = text.replace(text[start:end], var + " = " + str(new_value))
            #             (is_satisfy_condition, res) = verify_condition_new_text(new_text)
            #             if is_satisfy_condition:
            #                 new_question = gemini_generate_new_question(index, text, var, new_text, new_value, gemini_model)
            #                 if llm_attack(new_question, res, vllm_model) == False:
            #                     return (new_text, var, new_value, res, new_question)
            #         tmp += 0.05
            # case 8
            # if value > 1 and (value/0.1)%1==0:
            #     # print('vo case 0.1 >10')
            #     tmp = 0.5
            #     while tmp < max(10, value*2):
            #         new_value = value + tmp
            #         start = text.find(var + " = ")
            #         for j in range(start, len(text)):
            #             if text[j:j+4] == " ###":
            #                 end = j
            #                 break
            #         if text[start:end] in text:
            #             new_text = text.replace(text[start:end], var + " = " + str(new_value))
            #             (is_satisfy_condition, res) = verify_condition_new_text(new_text)
            #             if is_satisfy_condition:
            #                 new_question = gemini_generate_new_question(index, text, var, new_text, new_value, vllm_model)
            #                 new_question_list.append(new_question)
            #                 new_pcot_answer_list.append(new_text)                            
            #                 # if llm_attack(new_question, res, vllm_model) == False:
            #                 # return (new_text, var, new_value, res, new_question)
            #         tmp += 0.5
            # case 9
            # if value > 1 and (value/0.25)%1==0:
            #     # print('vo case 0.25')
            #     tmp = 0.25
            #     while tmp < max(10, value*2):
            #         new_value = value + tmp
            #         start = text.find(var + " = ")
            #         for j in range(start, len(text)):
            #             if text[j:j+4] == " ###":
            #                 end = j
            #                 break
            #         if text[start:end] in text:
            #             new_text = text.replace(text[start:end], var + " = " + str(new_value))
            #             (is_satisfy_condition, res) = verify_condition_new_text(new_text)
            #             if is_satisfy_condition:
            #                 new_question = gemini_generate_new_question(index, text, var, new_text, new_value, vllm_model)
            #                 new_question_list.append(new_question)
            #                 new_pcot_answer_list.append(new_text)  
            #                 # if llm_attack(new_question, res, vllm_model) == False:
            #                 # return (new_text, var, new_value, res, new_question)
            #         tmp += 0.25
            

    assert len(new_question_list) == len(new_pcot_answer_list)

    with open(f'data/pcot/MATH/algebra/new_question/{index}.jsonl', 'w') as fw:
        for line in new_question_list:
            fw.write(
                json.dumps(line) + '\n'
            )

    with open(f'data/pcot/MATH/algebra/new_pcot/{index}.jsonl', 'w') as fw:
        for line in new_pcot_answer_list:
            fw.write(
                json.dumps(line) + '\n'
            )
            # if value > 1 and (value/0.01)%1==0 and value%1!=0:
            #     tmp = 0.01
            #     while tmp < max(10, value*2):
            #         new_value = value + tmp
            #         start = text.find(var + " = ")
            #         for j in range(start, len(text)):
            #             if text[j:j+4] == " ###":
            #                 end = j
            #                 break
            #         if text[start:end] in text:
            #             new_text = text.replace(text[start:end], var + " = " + str(new_value))
            #             (is_satisfy_condition, res) = verify_condition_new_text(new_text)
            #             if is_satisfy_condition:
            #                 new_question = gemini_generate_new_question(index, text, var, new_text, new_value, gemini_model)
            #                 if llm_attack(new_question, res, vllm_model) == False:
            #                     return (new_text, var, new_value, res, new_question)
            #         tmp += 0.01

    if len(new_pcot_answer_list) == 0:
        print(f'File {index} can not generate new question.')
    return None



if __name__ == "__main__":

    for index in tqdm(ids):
        if index == 1166:
            try:
                print(index)
                with open(f'data/pcot/MATH/algebra/original_pcot/{index}.py') as fr:
                    text = fr.read().replace('//', '/')

                conditions = extract_conditions(text)    
                parsed = ast.parse(text)
                variables_dict = {}
                local_vars = {}
                for node in parsed.body:
                    if isinstance(node, ast.Assign):
                        var_name = node.targets[0].id
                        var_value = eval_expr(node.value, local_vars)
                        local_vars[var_name] = var_value 
                        
                        variables_dict[var_name] = {
                            "value": var_value,
                            "condition": conditions.get(var_name, {})
                        }
                change_one_value(text, variables_dict, index)
            except:
                continue

            # if new_change:
            #     new_text, var, new_value, res, new_question = new_change
                
            #     with open(f'data/pcot/MATH/algebra/new_question/{index}.txt', 'w') as fw:
            #         fw.write(new_question)
            #     # with open(f'data/gen_new_question_change_1_value_prompt/{index}.txt', 'w') as fw:
            #     #     fw.write(prompt)
            #     with open(f'data/pcot/MATH/algebra/new_pcot/{index}.py', 'w') as fw:
            #         fw.write(new_text)
            # else:
            #     print(f'file {index} is error!!!')