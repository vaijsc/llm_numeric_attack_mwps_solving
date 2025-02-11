# Define the value of x
x = -2  ### condition: 'x': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate 2 * x^2
term1 = 2 * (x ** 2)  ### condition: 'term1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate 3 * x
term2 = 3 * x  ### condition: 'term2': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Define the constant term
constant_term = 4  ### condition: 'constant_term': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the final value
final_value = term1 + term2 + constant_term  ### condition: 'final_value': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the final value
print(f"The value of 2x^2 + 3x + 4 is: {final_value}")