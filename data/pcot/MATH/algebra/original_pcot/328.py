# Define the value of x to evaluate the function
x = 1  ### condition: 'x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the coefficient and constant for the linear function
coefficient = 5  ### condition: 'coefficient': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
constant = 4  ### condition: 'constant': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the value of the function f(x)
f_x = coefficient * x + constant  ### condition: 'f_x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of f(1)
print(f"f(1) = {f_x}")