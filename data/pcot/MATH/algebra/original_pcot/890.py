# Define the value of the infinite nested square root expression
nested_sqrt_value = 9  ### condition: 'nested_sqrt_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Rearranging the equation gives us x + sqrt(x + sqrt(x + ...)) = 9^2
# Calculate the square of the nested square root value
square_of_nested_sqrt = nested_sqrt_value ** 2  ### condition: 'square_of_nested_sqrt': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate x by solving the equation x + sqrt(x + sqrt(x + ...)) = 81
# This implies x + 9 = 81
# Therefore, x = 81 - 9
x = square_of_nested_sqrt - nested_sqrt_value  ### condition: 'x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of x
print(f"The value of x is: {x}")