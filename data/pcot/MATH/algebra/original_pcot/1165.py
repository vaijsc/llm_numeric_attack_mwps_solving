# Define the value of x at which we want to evaluate the function g
x = 0  ### condition: 'x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the coefficients in the function g(x)
coefficient = 3  ### condition: 'coefficient': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
constant = 4  ### condition: 'constant': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate g(x) using the defined function
g_x = coefficient * x - constant  ### condition: 'g_x': {'type': 'int', '<=': None, '>=': -4, 'science_constant': False, 'direct_from_question': False}
# Print the result of g(0)
print(f"g(0) = {g_x}")