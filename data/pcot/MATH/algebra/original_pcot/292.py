# Define the input value for x to evaluate f(x)
x_f = 1  ### condition: 'x_f': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the input value for x to evaluate g(x)
x_g = 2  ### condition: 'x_g': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate f(1) using the function f(x) = 5x + 2
f_x_f = 5 * x_f + 2  ### condition: 'f_x_f': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate f(f(1))
f_f_x_f = 5 * f_x_f + 2  ### condition: 'f_f_x_f': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate g(2) using the function g(x) = 3x^2 - 4x
g_x_g = 3 * (x_g ** 2) - 4 * x_g  ### condition: 'g_x_g': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate g(g(2))
g_g_x_g = 3 * (g_x_g ** 2) - 4 * g_x_g  ### condition: 'g_g_x_g': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the final expression f(f(1)) - g(g(2))
final_result = f_f_x_f - g_g_x_g  ### condition: 'final_result': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"f(f(1)) - g(g(2)) = {final_result}")