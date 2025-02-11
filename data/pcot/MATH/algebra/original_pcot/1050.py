# Define the input value
x = -1  ### condition: 'x': {'type': 'int', '<=': None, '>=': -1, 'science_constant': False, 'direct_from_question': True}
# Calculate f(x) = 5x + 3
f_x = 5 * x + 3  ### condition: 'f_x': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate g(f(x)) = (f(x))^2 - 2
g_f_x = f_x ** 2 - 2  ### condition: 'g_f_x': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the result of g(f(-1))
print(f"g(f(-1)) = {g_f_x}")