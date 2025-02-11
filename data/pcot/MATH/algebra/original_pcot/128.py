# Define the coefficient of x^2 in the equation of the parabola
a = 2  ### condition: 'a': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
# Define the coefficient of x in the equation of the parabola
b = -4  ### condition: 'b': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the x-coordinate (m) of the vertex of the parabola using the formula m = -b / (2a)
m = -b / (2 * a)  ### condition: 'm': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Since m is computed from the equation, its type should be considered as int in context
m = int(m)  ### condition: 'm': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the x-coordinate of the vertex of the parabola
print(f"The x-coordinate (m) of the vertex of the parabola is: {m}")