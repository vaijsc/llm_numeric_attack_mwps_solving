# Define the variable x as a real number
x = 0.0 ### condition: 'x': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}

# Define constants for the coefficients and terms in the expression
coeff_1 = 49 ### condition: 'coeff_1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
coeff_2 = 14 ### condition: 'coeff_2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
term_1 = 19 ### condition: 'term_1': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
term_2 = 7 ### condition: 'term_2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}

# Calculate each part of the expression
part_1 = coeff_1 * x**2 ### condition: 'part_1': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
part_2 = coeff_2 * x * (term_1 - term_2 * x) ### condition: 'part_2': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
part_3 = (term_1 - term_2 * x)**2 ### condition: 'part_3': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}

# Calculate the final expression
result = part_1 + part_2 + part_3 ### condition: 'result': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}

# Print the result
print(f"The value of the expression is: {result}")
