# Define the input value for g(x)
input_value = 2  ### condition: 'input_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate g(2)
g_x = input_value**2 + 3  ### condition: 'g_x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate f(g(2))
f_g_x = 2 * g_x - 4  ### condition: 'f_g_x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the result of f(g(2))
print(f"f(g(2)) = {f_g_x}")