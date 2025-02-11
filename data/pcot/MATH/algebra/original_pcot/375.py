# Define the input value for g(x)
x_value = 1  ### condition: 'x_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate g(x) = 2x - 4
g_x = 2 * x_value - 4  ### condition: 'g_x': {'type': 'int', '<=': None, '>=': -4, 'science_constant': False, 'direct_from_question': False}
# Calculate f(g(x)) = (4 - g(x)) / 2
f_g_x = (4 - g_x) / 2  ### condition: 'f_g_x': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate f(x) = (4 - x) / 2
f_x = (4 - x_value) / 2  ### condition: 'f_x': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate g(f(x)) = 2 * f(x) - 4
g_f_x = 2 * f_x - 4  ### condition: 'g_f_x': {'type': 'float', '<=': None, '>=': -4, 'science_constant': False, 'direct_from_question': False}
# Calculate the final result f(g(1)) * g(f(1))
result = f_g_x * g_f_x  ### condition: 'result': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"f(g(1)) * g(f(1)) = {result}")