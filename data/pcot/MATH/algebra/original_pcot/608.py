# Define the value of the constant in the equation
constant_value = 5  ### condition: 'constant_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the value of x using the given equation
x_value = constant_value ** 2 - constant_value  ### condition: 'x_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of x
print(f"The value of x is: {x_value}")