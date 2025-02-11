# Define the value of x
x = 13  ### condition: 'x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the value of y
y = 5  ### condition: 'y': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the expression (x + y)
x_plus_y = x + y  ### condition: 'x_plus_y': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the expression (x - y)
x_minus_y = x - y  ### condition: 'x_minus_y': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the final result of (x + y)(x - y)
result = x_plus_y * x_minus_y  ### condition: 'result': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"Evaluation of (x + y)(x - y): {result}")