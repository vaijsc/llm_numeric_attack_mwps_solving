# Define the coefficient and variable of the expression
coefficient = 4  ### condition: 'coefficient': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the power of the variable
a_power = 2  ### condition: 'a_power': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the exponent to which the expression is raised
exponent = 3  ### condition: 'exponent': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the new coefficient after exponentiation
new_coefficient = coefficient ** exponent  ### condition: 'new_coefficient': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the new power of the variable
new_a_power = a_power * exponent  ### condition: 'new_a_power': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the simplified expression
print(f"Simplified expression: {new_coefficient}a^{new_a_power}")