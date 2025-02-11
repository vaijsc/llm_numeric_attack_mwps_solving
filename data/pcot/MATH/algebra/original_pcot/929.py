# Define the value of a
a = -1  ### condition: 'a': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the value of b
b = 5  ### condition: 'b': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate b squared
b_squared = b ** 2  ### condition: 'b_squared': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the value of the expression
expression_value = -a - b_squared + 3 * a * b  ### condition: 'expression_value': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the value of the expression
print(f"The value of the expression is: {expression_value}")