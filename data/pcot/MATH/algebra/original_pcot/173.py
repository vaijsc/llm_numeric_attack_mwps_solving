# Define the value of x for the function h(x)
x = 6  ### condition: 'x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate x^3
x_cubed = x ** 3  ### condition: 'x_cubed': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Add 72 to x^3
numerator = x_cubed + 72  ### condition: 'numerator': {'type': 'int', '<=': None, '>=': 72, 'science_constant': False, 'direct_from_question': False}
# Define the divisor
divisor = 2  ### condition: 'divisor': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
# Calculate the division of the numerator by the divisor
division_result = numerator / divisor  ### condition: 'division_result': {'type': 'float', '<=': None, '>=': 36, 'science_constant': False, 'direct_from_question': False}
# Calculate the square root of the division result
sqrt_result = division_result ** 0.5  ### condition: 'sqrt_result': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Add 1 to the square root result to get h(x)
h_x = sqrt_result + 1  ### condition: 'h_x': {'type': 'float', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': False}
# Print the value of h(6)
print(f"The value of h(6) is: {h_x}")