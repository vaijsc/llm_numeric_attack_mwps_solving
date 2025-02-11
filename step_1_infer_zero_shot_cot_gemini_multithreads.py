import google.generativeai as genai
from utils import get_examples_gsm8k, GSMDataset, extract_answer, return_predicted_answer, safety_settings
from utils import maybe_remove_comma, find_number
import re
import collections
import torch
from tqdm import tqdm
import json
from datasets import load_dataset
from concurrent.futures import ThreadPoolExecutor, as_completed
import os

# Define constants and configurations
PROMPT = """### Instruction: {question}
Let’s think step by step.
### Response:"""
ANS_RE = re.compile(r"#### (\-?[0-9\.\,]+)")
INVALID_ANS = "[invalid]"
PATTERN = r"(?:\(|\s)([A-Z])\.?(?:\)|\s|$)"

GOOGLE_API_KEY = "AIzaSyBLaB5zJKfZTcMD2FgTWRVc2oM0s2lb8YI"  # Insert your API key here
genai.configure(api_key=GOOGLE_API_KEY)
gemini_model = genai.GenerativeModel('gemini-1.5-flash', safety_settings=safety_settings)
print('Gemini model: ', gemini_model)

# Dataset and saving path
ds = load_dataset("lighteval/MATH", "geometry")['test']
save_path = 'results/gemini/zero_shot_original/MATH/geometry'
os.makedirs(save_path, exist_ok=True)

# Function to process each example
def extract_answer_predict(response):
    short_responses = maybe_remove_comma(find_number(response))
    return short_responses

def get_response(prompt, model):
    output = []
    while len(output) < 5:
        response = model.generate_content(prompt)
        if response.text.replace('\n\n\n', '\n').replace('\n\n', '\n') not in output:
            output.append(response.text.replace('\n\n\n', '\n').replace('\n\n', '\n'))
    return output

def gemini_inference(example, model):
    q_prompt = PROMPT.format(question=example['problem'])
    responses = get_response(q_prompt, model)
    ans = [extract_answer_predict(response) for response in responses]
    counter = collections.Counter(ans[:30])
    pred_res = counter.most_common(1)[0][0]
    example['prompt'] = q_prompt
    example['responses'] = responses
    example['pred_answers'] = pred_res
    example['final_pred_answer'] = ans
    example['ground_truth'] = extract_answer_predict(example['solution'])
    return example

# Function to run inference and save results for each example
def process_example(idx, example, model):
    # Run inference
    result = gemini_inference(example, model)
    # Save to JSON file
    with open(os.path.join(save_path, f'{idx}.json'), 'w') as fw:
        json.dump(result, fw, indent=4)
    return idx  # Return idx to confirm completion

# Run ThreadPoolExecutor for parallel processing
num_threads = 16 # Adjust the number of threads based on available resources
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    futures = {executor.submit(process_example, idx, example, gemini_model): idx for idx, example in enumerate(ds) if idx < 312}

    # Track progress with as_completed
    for future in tqdm(as_completed(futures), total=len(ds), desc="Processing Examples"):
        idx = futures[future]
        try:
            future.result()  # Ensure any exceptions are raised
        except Exception as e:
            print(f"Error processing example {idx}: {e}")
