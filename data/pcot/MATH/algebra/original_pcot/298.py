# Define the value of x for which we want to calculate f(x)
x = 3  ### condition: 'x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate g(x) using the given function g(x) = 2x - 1
g_x = 2 * x - 1  ### condition: 'g_x': {'type': 'int', '<=': None, '>=': -1, 'science_constant': False, 'direct_from_question': False}
# Calculate g(g(x)), which means applying g to g(x)
g_g_x = 2 * g_x - 1  ### condition: 'g_g_x': {'type': 'int', '<=': None, '>=': -1, 'science_constant': False, 'direct_from_question': False}
# Calculate f(x) using the formula f(x) = g(g(x)) - g(x)
f_x = g_g_x - g_x  ### condition: 'f_x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of f(3)
print(f"f(3) = {f_x}")