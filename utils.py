import google.generativeai as genai
from torch.utils.data import DataLoader
import asyncio
from typing import Any
from typing import Any, Callable, Iterable, Match, Optional, Pattern, Protocol, Sequence, Union
import pickle
import base64
import requests
from io import BytesIO
import json
import os
import re
import torch as th
from tqdm import tqdm
from torch.utils.data import DataLoader
import sys
import pickle
import time
from typing import List
from math import ceil, log


ANS_RE = re.compile(r"#### (\-?[0-9\.\,]+)")
INVALID_ANS = "[invalid]"
PATTERN = r"(?:\(|\s)([A-Z])\.?(?:\)|\s|$)"

GOOGLE_API_KEY="AIzaSyB8RHWmEcDqJ3DZM-oM6uehEXzVEgMvfGg"
genai.configure(api_key=GOOGLE_API_KEY)
# safety_settings=[
#     {
#         "category": "HARM_CATEGORY_HARASSMENT",
#         "threshold": "BLOCK_NONE",
#     },
#     {
#         "category": "HARM_CATEGORY_HATE_SPEECH",
#         "threshold": "BLOCK_NONE",
#     },
#     {
#         "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
#         "threshold": "BLOCK_NONE",
#     },
#     {
#         "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
#         "threshold": "BLOCK_NONE",
#     },
# ]
safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]
model = genai.GenerativeModel('gemini-pro', safety_settings = safety_settings)


class GSMDataset(th.utils.data.Dataset):
    def __init__(self, examples):
        self.examples = examples
        self.qns = [ex["question"] for ex in self.examples]
        self.ans = [ex["answer"] for ex in self.examples]
        self.ids = [idx for idx, ex in enumerate(self.examples)]

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, idx):
        qn = self.qns[idx]
        ans = self.ans[idx]
        qid = self.ids[idx]
        
        return qid, qn, ans

def read_jsonl(path: str):
    with open(path) as fh:
        return [json.loads(line) for line in fh.readlines() if line]

def get_examples_gsm8k(split, lr=0, rr=-1):
    path = f"data/gsm8k/{split}.jsonl"
    print("path: ", path)
    examples = read_jsonl(path)

    for ex in examples:
        ex.update(question=ex["question"] + "\n")
        ex.update(answer=ex["answer"] + "<|endoftext|>")

    if rr == -1:
        examples = examples[lr:len(examples)]
    else:
        examples = examples[lr:rr]
        
    print(f"{len(examples)} {split} examples")
    return examples


def extract_answer(completion):
    match = ANS_RE.search(completion)
    if match:
        match_str = match.group(1).strip()
        match_str = match_str.replace(",", "")
        return match_str
    else:
        return INVALID_ANS

def get_response(prompt):
    response = model.generate_content(prompt)
    return response.text
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def maybe_remove_comma(x: str) -> str:
    if is_float(x):
        return x
    return x.replace(',', '')

def find_numbers(x: str) -> List[str]:
    numbers = re.compile(
      r'-?[\d,]*\.?\d+',
      re.MULTILINE | re.DOTALL | re.IGNORECASE,
      ).findall(x)
    return numbers


def find_number(x: str, answer_delimiter: Optional[str] = 'Answer:') -> str:
    if answer_delimiter in x:
        answer = x.split(answer_delimiter)[-1]
        numbers = find_numbers(answer)
        if numbers:
            return numbers[0]

    numbers = find_numbers(x)
    if numbers:
        return numbers[-1]
    return ''
def return_predicted_answer(question_answer_list):
    correct = 0
    for out in question_answer_list:
        soln = out['generated_text'].split('\nQ:')[0]
        short_responses = maybe_remove_comma(find_number(soln))
        
        if short_responses != '':
            correct += float(maybe_remove_comma(find_number(out['answer']))) == float(short_responses)
            out['is_correct'] = int(float(maybe_remove_comma(find_number(out['answer']))) == float(short_responses))
            out['predict'] = short_responses
        else:
            out['is_correct'] = 0
            out['predict'] = "-10000000000"
    print("len question answer list: ", question_answer_list)
    print("question answer list: ", question_answer_list)    
    print('Accuracy: ', correct/(1.0*len(question_answer_list)))
    return question_answer_list


import ast
import re
import json 
from tqdm import tqdm
import google.generativeai as genai
# Function to extract conditions from the comments
def extract_conditions(text):
    condition_pattern = r"### condition: '(.*?)': ({.*?})"
    matches = re.findall(condition_pattern, text, re.DOTALL)
    conditions = {var: eval(cond) for var, cond in matches}
    return conditions

# def eval_expr(node, local_vars):
#     if isinstance(node, ast.BinOp):
#         left = eval_expr(node.left, local_vars)
#         right = eval_expr(node.right, local_vars)
#         if isinstance(node.op, ast.Add):
#             return left + right
#         elif isinstance(node.op, ast.Sub):
#             return left - right
#         elif isinstance(node.op, ast.Mult):
#             return left * right
#         elif isinstance(node.op, ast.Div):
#             return left / right
#         elif isinstance(node.op, ast.Pow):  # Handle exponentiation
#             return left ** right
#         elif isinstance(node.op, ast.Mod):  # Handle modulus
#             return left % right
#     elif isinstance(node, ast.Num):
#         return node.n
#     elif isinstance(node, ast.Name):
#         return local_vars[node.id]
#     elif isinstance(node, ast.Call):
#         if node.func.id == 'round':
#             return round(eval_expr(node.args[0], local_vars))
#         elif node.func.id == 'abs':
#             return abs(eval_expr(node.args[0], local_vars))
#         elif node.func.id == 'max':
#             return max(eval_expr(node.args[0], local_vars), eval_expr(node.args[1], local_vars))
#         func_name = node.func.id
#         args = [eval_expr(arg, local_vars) for arg in node.args]
#         if func_name == 'sum':
#             return sum(args[0])
#         elif func_name == 'min':
#             return min(args[0])
#         elif func_name == 'round':
#             return round(args[0])
#         elif func_name == 'int':
#             return int(args[0])
#     elif isinstance(node, ast.List):
#         return [eval_expr(elt, local_vars) for elt in node.elts]
#     elif isinstance(node, ast.Compare):
#         if isinstance(node.ops[0], ast.Gt):
#             left = eval_expr(node.left, local_vars)
#             right = eval_expr(node.comparators[0], local_vars)
#             return left > right
#     elif isinstance(node, ast.UnaryOp):
#         if isinstance(node.op, ast.USub):  # Check for unary minus
#             return -eval_expr(node.operand, local_vars)

from fractions import Fraction

import ast
from math import ceil


def eval_expr(node, local_vars):
    if isinstance(node, ast.BinOp):
        left = eval_expr(node.left, local_vars)
        right = eval_expr(node.right, local_vars)
        if isinstance(node.op, ast.Add):
            return left + right
        elif isinstance(node.op, ast.Sub):
            return left - right
        elif isinstance(node.op, ast.Mult):
            return left * right
        elif isinstance(node.op, ast.Div):
            return left / right
        elif isinstance(node.op, ast.Pow):
            return left ** right
        elif isinstance(node.op, ast.Mod):
            return left % right
    elif isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.Name):
        return local_vars.get(node.id, None)
    elif isinstance(node, ast.Constant):  # Handle literals in Python 3.8+
        return node.value
    elif isinstance(node, ast.Call):
        # Check if the function is a simple name
        func_name = None
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
        elif isinstance(node.func, ast.Attribute):  # Handle attributes like math.sqrt
            func_name = node.func.attr

        args = [eval_expr(arg, local_vars) for arg in node.args]
        
        if func_name == 'round':
            if isinstance(args[0], complex):  # Handle complex numbers
                real_part = round(args[0].real)
                imag_part = round(args[0].imag)
                return complex(real_part, imag_part)
            return round(args[0])
        
        if func_name == 'round':
            return round(args[0])
        elif func_name == 'abs':
            return abs(args[0])
        elif func_name == 'max':
            return max(args)
        elif func_name == 'sum':
            return sum(args[0])
        elif func_name == 'min':
            return min(args[0])
        elif func_name == 'int':
            return int(args[0])
        elif func_name == 'limit_denominator':
            # Check if the argument is already a Fraction
            if isinstance(args[0], Fraction):
                if len(args) > 1:
                    return args[0].limit_denominator(args[1])
                return args[0].limit_denominator()
            else:
                raise TypeError
        elif func_name == 'ceil':
            return ceil(args[0])
        elif func_name == "set":  # Add support for `set`
            return set(args)
        elif func_name == 'log':
            # Support optional base argument for log
            return log(args[0]) if len(args) == 1 else log(args[0], args[1])
        else:
            raise ValueError(f"Unknown function '{func_name}' in expression")
    elif isinstance(node, ast.List):
        return [eval_expr(elt, local_vars) for elt in node.elts]
    elif isinstance(node, ast.Compare):
        if isinstance(node.ops[0], ast.Gt):
            left = eval_expr(node.left, local_vars)
            right = eval_expr(node.comparators[0], local_vars)
            return left > right
    elif isinstance(node, ast.UnaryOp):
        if isinstance(node.op, ast.USub):
            return -eval_expr(node.operand, local_vars)
    elif isinstance(node, ast.IfExp):  # Handle conditional expressions
        condition = eval_expr(node.test, local_vars)
        if condition:
            return eval_expr(node.body, local_vars)
        else:
            return eval_expr(node.orelse, local_vars)
    elif isinstance(node, ast.Lambda):  # Handle lambda expressions
        # Extract argument names
        arg_names = [arg.arg for arg in node.args.args]

        # Return a Python lambda function that evaluates the body with the given args
        return lambda *args: eval_expr(node.body, {**local_vars, **dict(zip(arg_names, args))})
  
    else:
        raise TypeError(f"Unsupported node type: {type(node).__name__}")

# def check_condition(value, condition):
#     # Ensure type
#     if not isinstance(value, eval(condition['type'])):
#         if isinstance(value, float) and condition['type'] == 'int' and value == int(value):
#             pass 
#         elif isinstance(value, int) and condition['type'] == 'float' and value == int(value):
#             pass
#         else:
#             return False
#     # Check lower bound
#     if condition['>='] is not None and isinstance(condition['>='], str) == False and  value < condition['>=']:
#         return False
#     # Check upper bound
#     if condition['<='] is not None and isinstance(condition['<='], str) == False and value > condition['<=']:
#         return False
#     # If there is a reference to another variable
#     if isinstance(condition['<='], str):
#         if value > variables_dict[condition['<=']]['value']:
#             return False
#     if isinstance(condition['>='], str):
#         if value < variables_dict[condition['>=']]['value']:
#             return False
#     # If specific value is required from the question
#     if condition['direct_from_question']:
#         pass  # Additional logic for this condition can be added as needed
    
#     return True

def check_condition(value, condition, variables_dict):
    # Ensure type
    if not isinstance(value, eval(condition['type'])):
        if isinstance(value, float) and condition['type'] == 'int' and value == int(value):
            pass 
        elif isinstance(value, int) and condition['type'] == 'float' and value == int(value):
            pass
        
        else:
            return False
    # Check lower bound
    if condition['>='] is not None and isinstance(condition['>='], str) == False and  value < condition['>=']:
        return False
    # Check upper bound
    if condition['<='] is not None and isinstance(condition['<='], str) == False and value > condition['<=']:
        return False
    # If there is a reference to another variable
    if isinstance(condition['<='], str):
        if value > variables_dict[condition['<=']]['value']:
            return False
    if isinstance(condition['>='], str):
        if value < variables_dict[condition['>=']]['value']:
            return False
    # If specific value is required from the question
    if condition['direct_from_question']:
        pass  # Additional logic for this condition can be added as needed
    return True



safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]