# Define the input value for the function f(x)
x_value = 8  ### condition: 'x_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the inner value for the square root
inner_value = 2 * x_value - 7  ### condition: 'inner_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Assert that the inner value is non-negative to ensure the square root is defined
assert inner_value >= 0, "The inner value must be non-negative for the square root."
# Calculate the square root of the inner value
square_root_value = inner_value ** 0.5  ### condition: 'square_root_value': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the value of the function f(x)
f_x_value = 3 * square_root_value - 8  ### condition: 'f_x_value': {'type': 'float', '<=': None, '>=': -8, 'science_constant': False, 'direct_from_question': False}
# Print the value of f(8)
print(f"f(8) = {f_x_value}")