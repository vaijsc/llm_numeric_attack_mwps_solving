# Define the value of a
a = 3  ### condition: 'a': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the value of b
b = 5  ### condition: 'b': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the expression a^2 + 2ab + b^2
expression_value = a**2 + 2*a*b + b**2  ### condition: 'expression_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the result of the expression
print(f"The value of (a) x (b) when a = {a} and b = {b} is: {expression_value}")