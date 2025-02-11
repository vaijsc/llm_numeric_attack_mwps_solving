PROMPT = """We have: 
Question: 
{question}
Answer:
```{answer}```

I want to change {var_name} = {new_value} the new answer is:
```{new_answer}```
Generate a new question, note that the words in the question and the context are not changed, only the variable value.
Put new question in <question></question> tags, return enought information in question.
Question:
"""