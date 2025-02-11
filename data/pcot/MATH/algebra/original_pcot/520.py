# Define the variable u
u = 0  ### condition: 'u': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the first expression (u + 4)(u - 1)
first_expression = (u + 4) * (u - 1)  ### condition: 'first_expression': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Define the second expression (u - 3)(u + 6)
second_expression = (u - 3) * (u + 6)  ### condition: 'second_expression': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the result of the entire expression
result = first_expression - second_expression  ### condition: 'result': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the result of the simplified expression
print(f"Simplified result: {result}")