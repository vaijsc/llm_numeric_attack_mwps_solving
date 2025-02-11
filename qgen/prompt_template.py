# QGEN_PROMPT= """
# You are a synthetic question generator.
# - Given a chunk of context, generate an question answered using solely the information from the context chunk. 
# - The question requires mixed information in the context to answer.
# - Include domain specific terms in the question.
# - Put the question in <question></question> tags
#
# # Context:
# {context}
#
# # Question:
# """.strip()
QGEN_PROMPT= """
You are a synthetic question generator.
- Given a chunk of context, generate questions answered using solely the information from the context chunk.
- 5 questions requires basic information in the context to answer.
- 5 questions requires mixed information in the context to answer. 
- Include domain-specific terms in the question.
- Put the question in <question></question> tags.

# Context:
{context}

# Question:
""".strip()

QGEN_PROMPT_WITH_META_DATA = """
You are a synthetic question generator.
- Given a chunk of context, generate questions answered using solely the information from the context chunk.
- 5 questions requires basic information in the context to answer.
- 5 questions requires mixed information in the context to answer. 
- Include domain-specific terms in the question.
- Put the question in <question></question> tags.
- Specify company name and year in the question using meta data.

# Meta data:
{meta}

# Context:
{context}

# Question:
""".strip()

QGEN_PROMPT_CUSTOM = """
You are a synthetic question generator.
- Given a chunk of context, generate an question answered using solely the information from the context chunk. 
- The question requires mixed information in the context to answer.
- Include domain specific terms in the question.
- Put the question in <question></question> tags

# Context:
{example_context}

# Question:
<question>{example_question}</question>

# Context:
{context}

# Question:
""".strip()

ANSWER_PROMPT = """
You are an AI assistant to answer a question using soly information from a given context. You have to write a proper answer to the given question. Your answer have to be concise and relevant to the question. Do not make a verbose answer and make it super clear. If there is no correct answer, response "I don't know"

# Context:
{context}

# Question:
{question}
""".strip()

ANSWER_PROMPT_WITH_META_DATA = """
You are an AI assistant to answer a question using soly information from a given context. You have to write a proper answer to the given question. Your answer have to be concise and relevant to the question. Do not make a verbose answer and make it super clear. If there is no correct answer, response "I don't know"

# Meta data:
{meta}

# Context:
{context}

# Question:
{question}
""".strip()

FILTER_NO_ANSWER_PROMPT = """
The following sentence is an answer of a question. You have to decide if the answer implies "I don't know". Think and give a short and concise explaination. If answer implies "I don't know", put <verdict>true</verdict>  at then end of your response. If not, put <verdict>false</verdict> at the end of your response.

# Answer:
Unfortunately the answer can not be found in the context.
# Explaination:
This sentence implies "I don't know".
# Verdict:
<verdict>true</verdict>

# Answer:
The final result is 100.
# Explaination:
This sentence contains a feasible answer.
# Verdict:
<verdict>false</verdict>

# Answer:
I have no answer.
# Explaination:
This sentence implies "I don't know".
# Verdict:
<verdict>true</verdict>

# Answer:
{answer}
""".strip()

FILTER_CONTEXT_DEPENDENT_PROMPT = """
You are a classifier that recognizes 'context-dependent' questions. A 'context-dependent' question has an answer that will change depending on the chosen context.  Give a concise explaination then put <verdict>true</verdict> at the end fo your response if the question is 'context-dependent', otherwise, put <verdict>false</verdict> at the end of your response.

# Question:
What is the highest score according to the table?
# Explaination:
This sentence is a 'context-dependent' question because "the table" is not determined.
# Verdict:
<verdict>true</verdict>

# Question:
What is the highest number of goals in a professional football match?
# Explaination:
This sentence is a good question because all entities are clear.
# Verdict:
<verdict>false</verdict>

# Question:
According to the essay, what is the main idea that the author implies?
# Explaination:
This sentence is a 'context-dependent' question because "the essay" is not determined.
# Verdict:
<verdict>true</verdict>

# Question:
What is the capital of Vietnam?
# Explaination:
This sentence is a good question because all entities are clear.
# Verdict:
<verdict>false</verdict>

#Question:
{question}
""".strip()
