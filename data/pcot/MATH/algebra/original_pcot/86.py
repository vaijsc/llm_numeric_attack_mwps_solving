# Define the base of the logarithm
base = 2  ### condition: 'base': {'type': 'int', '<=': None, '>=': 2, 'science_constant': False, 'direct_from_question': True}
# Define the number to evaluate the logarithm of
number = 1  ### condition: 'number': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Since log_b(a) = c can be rewritten as b^c = a, we directly know log_2(1) = 0
logarithm_result = 0  ### condition: 'logarithm_result': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the result of the logarithm
print(f"log_{base}{number} = {logarithm_result}")