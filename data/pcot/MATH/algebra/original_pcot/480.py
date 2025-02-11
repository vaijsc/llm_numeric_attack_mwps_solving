# Define the variable p
p = 2.0  ### condition: 'p': {'type': 'float', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': False}
# Define the variable q using the relationship given in the problem
q = 2.0  ### condition: 'q': {'type': 'float', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': False}
# Calculate (p-1) and (q-1)
p_minus_1 = p - 1  ### condition: 'p_minus_1': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
q_minus_1 = q - 1  ### condition: 'q_minus_1': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate (p-1)(q-1)
result = p_minus_1 * q_minus_1  ### condition: 'result': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"The value of (p-1)(q-1) is: {result}")