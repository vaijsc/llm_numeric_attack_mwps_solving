# Define the coefficient of x^2 in the quadratic expression
a = 1  ### condition: 'a': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
# Define the coefficient of x in the quadratic expression
b = -6  ### condition: 'b': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the constant term in the quadratic expression
c = 13  ### condition: 'c': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the vertex x-coordinate using the formula -b/(2a)
vertex_x = -b / (2 * a)  ### condition: 'vertex_x': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the minimum value of the quadratic expression at vertex_x
min_value = a * (vertex_x ** 2) + b * vertex_x + c  ### condition: 'min_value': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Since we need the smallest value as an integer, we will round it
smallest_value = int(min_value)  ### condition: 'smallest_value': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the smallest value of the expression
print(f"The smallest value of the expression x^2 - 6x + 13 is: {smallest_value}")