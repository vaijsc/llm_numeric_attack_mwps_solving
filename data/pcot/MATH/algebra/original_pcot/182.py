# Define the coefficients of the quadratic equation
a = 1  ### condition: 'a': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
b = 2  ### condition: 'b': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
c = -6  ### condition: 'c': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the x-coordinate of the vertex
vertex_x = -b / (2 * a)  ### condition: 'vertex_x': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the y-coordinate of the vertex
vertex_y = a * (vertex_x ** 2) + b * vertex_x + c  ### condition: 'vertex_y': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Define the coordinates of the point (4, 5)
point_x = 4  ### condition: 'point_x': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
point_y = 5  ### condition: 'point_y': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the distance between the vertex and the point (4, 5)
distance = ((vertex_x - point_x) ** 2 + (vertex_y - point_y) ** 2) ** 0.5  ### condition: 'distance': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the distance
print(f"The distance between the vertex and the point (4, 5) is: {distance}")