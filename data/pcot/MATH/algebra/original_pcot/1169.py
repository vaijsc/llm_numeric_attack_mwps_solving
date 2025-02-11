# Define the coefficients of the first polynomial
coeff_1_x2 = 9  ### condition: 'coeff_1_x2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
coeff_1_x = 3   ### condition: 'coeff_1_x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
constant_1 = 7  ### condition: 'constant_1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the coefficients of the second polynomial
coeff_2_x2 = 3   ### condition: 'coeff_2_x2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
coeff_2_x5 = 7   ### condition: 'coeff_2_x5': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
constant_2 = 2   ### condition: 'constant_2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Combine the coefficients for the like terms
total_coeff_x2 = coeff_1_x2 + coeff_2_x2  ### condition: 'total_coeff_x2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
total_coeff_x5 = coeff_2_x5                ### condition: 'total_coeff_x5': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
total_constant = constant_1 + constant_2   ### condition: 'total_constant': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the simplified polynomial in decreasing order of degree
print(f"Simplified polynomial: {total_coeff_x5}x^5 + {total_coeff_x2}x^2 + {total_constant}")