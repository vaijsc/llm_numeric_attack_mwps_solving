# Define the coefficient and exponent for the numerator
coefficient_num1 = 10  ### condition: 'coefficient_num1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
exponent_num1 = 3  ### condition: 'exponent_num1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
coefficient_num2 = 4  ### condition: 'coefficient_num2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
exponent_num2 = 6  ### condition: 'exponent_num2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the coefficient and exponent for the denominator
coefficient_den = 8  ### condition: 'coefficient_den': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
exponent_den = 4  ### condition: 'exponent_den': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the total coefficient for the numerator
total_coefficient_num = coefficient_num1 * coefficient_num2  ### condition: 'total_coefficient_num': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the total exponent for the numerator
total_exponent_num = exponent_num1 + exponent_num2  ### condition: 'total_exponent_num': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the total coefficient for the denominator
total_coefficient_den = coefficient_den  ### condition: 'total_coefficient_den': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the simplified coefficient
simplified_coefficient = total_coefficient_num // total_coefficient_den  ### condition: 'simplified_coefficient': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the simplified exponent
simplified_exponent = total_exponent_num - exponent_den  ### condition: 'simplified_exponent': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the simplified expression
print(f"Simplified expression: {simplified_coefficient}r^{simplified_exponent}")