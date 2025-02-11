import google.generativeai as genai
from utils import get_examples_gsm8k, GSMDataset, extract_answer, return_predicted_answer
from utils import extract_answer, return_predicted_answer, safety_settings
from utils import maybe_remove_comma, find_number
import re
import collections
import torch

PROMPT = """### Instruction: {question}
Let’s think step by step.
### Response:"""

ANS_RE = re.compile(r"#### (\-?[0-9\.\,]+)")
INVALID_ANS = "[invalid]"
PATTERN = r"(?:\(|\s)([A-Z])\.?(?:\)|\s|$)"
from tqdm import tqdm
import json 


# GOOGLE_API_KEY="AIzaSyBa7DeQ7t83ZmcGLumkRidj-Y
# FDRvHImdg"
genai.configure(api_key=GOOGLE_API_KEY)
gemini_model = genai.GenerativeModel('gemini-1.5-flash', safety_settings = safety_settings)
print('Gemini model: ', gemini_model)


a = ['viet mot bai van', 'viet mot bai tho']
responses = gemini_model.generate_content(a)