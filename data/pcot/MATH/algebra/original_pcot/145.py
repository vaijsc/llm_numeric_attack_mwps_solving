# Define the constant value of the function g(x)
g_x_constant = 3  ### condition: 'g_x_constant': {'type': 'int', '<=': None, '>=': 0, 'science_constant': True, 'direct_from_question': True}
# Define the input value for which we want to evaluate the function
input_value = 2  ### condition: 'input_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the value of g at the input value
g_at_input = g_x_constant  ### condition: 'g_at_input': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of g(2)
print(f"g(2) = {g_at_input}")