# Define the value of x
x = 7  ### condition: 'x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}

# Calculate the value of the expression 3x^2 + 5x - 1
expression_value = 3 * (x ** 2) + 5 * x - 1  ### condition: 'expression_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}

# Print the value of the expression
print(f"The value of the expression 3x^2 + 5x - 1 when x = {x} is: {expression_value}")