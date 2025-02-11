# Define the input value for g(x)
input_value_g = 7  ### condition: 'input_value_g': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate g(7)
g_output = input_value_g + 7  ### condition: 'g_output': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the input value for f(x)
input_value_f = 3  ### condition: 'input_value_f': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate f(3)
f_output = (input_value_f ** 2) - 1  ### condition: 'f_output': {'type': 'int', '<=': None, '>=': -1, 'science_constant': False, 'direct_from_question': False}
# Evaluate f(g(7))
f_of_g_output = (g_output ** 2) - 1  ### condition: 'f_of_g_output': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Evaluate g(f(3))
g_of_f_output = f_output + 7  ### condition: 'g_of_f_output': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the final result: f(g(7)) + g(f(3))
final_result = f_of_g_output + g_of_f_output  ### condition: 'final_result': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"f(g(7)) + g(f(3)) = {final_result}")