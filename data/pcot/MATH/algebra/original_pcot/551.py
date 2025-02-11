# Define the vertex coordinates
vertex_x = 2  ### condition: 'vertex_x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
vertex_y = 3  ### condition: 'vertex_y': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the point (4, 4) that lies on the parabola
point_x = 4  ### condition: 'point_x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
point_y = 4  ### condition: 'point_y': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the value of 'a' using the vertex form of a parabola
a = (point_y - vertex_y) / ((point_x - vertex_x) ** 2)  ### condition: 'a': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the value of x for which we want to find y
x_value = 6  ### condition: 'x_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the corresponding y value using the parabola equation
y_value = a * (x_value - vertex_x) ** 2 + vertex_y  ### condition: 'y_value': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of y when x=6
print(f"The value of y when x=6: {y_value}")