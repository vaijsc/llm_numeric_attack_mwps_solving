# Define the variable x
x = 0  ### condition: 'x': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate x^2
x_squared = x ** 2  ### condition: 'x_squared': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate 2x(5 - x)
two_x_times_five_minus_x = 2 * x * (5 - x)  ### condition: 'two_x_times_five_minus_x': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate (5 - x)^2
five_minus_x_squared = (5 - x) ** 2  ### condition: 'five_minus_x_squared': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the total expression x^2 + 2x(5 - x) + (5 - x)^2
total_expression = x_squared + two_x_times_five_minus_x + five_minus_x_squared  ### condition: 'total_expression': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the total expression
print(f"Value of the expression x^2 + 2x(5 - x) + (5 - x)^2: {total_expression}")