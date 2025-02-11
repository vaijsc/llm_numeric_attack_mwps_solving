# Define the value of x^2 + 1/x^2
x_squared_plus_one_over_x_squared = 7  ### condition: 'x_squared_plus_one_over_x_squared': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate x^4 + 1/x^4 using the identity: (x^2 + 1/x^2)^2 = x^4 + 2 + 1/x^4
x_four_plus_one_over_x_four = (x_squared_plus_one_over_x_squared ** 2) - 2  ### condition: 'x_four_plus_one_over_x_four': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of x^4 + 1/x^4
print(f"The value of x^4 + 1/x^4 is: {x_four_plus_one_over_x_four}")