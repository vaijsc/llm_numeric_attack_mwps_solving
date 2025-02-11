# Define the value of x
x_value = 2  ### condition: 'x_value': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the output of the piecewise function for x <= 2
output_under_equal_2 = 2 + (x_value - 2) ** 2  ### condition: 'output_under_equal_2': {'type': 'float', '<=': None, '>=': 2, 'science_constant': False, 'direct_from_question': False}
# Define the output of the piecewise function
output_k = output_under_equal_2  ### condition: 'output_k': {'type': 'float', '<=': None, '>=': 2, 'science_constant': False, 'direct_from_question': False}
# Define the value of f(x) for x > 2 which should match the output of the inverse
k_x_value = output_k  ### condition: 'k_x_value': {'type': 'float', '<=': None, '>=': 2, 'science_constant': False, 'direct_from_question': False}
# Print k(x) function for the required condition
print(f"Function k(x) such that f is its own inverse at x > 2: k(x) = {k_x_value}")