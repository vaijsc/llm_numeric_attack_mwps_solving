# Define the coordinates of the point
x_coordinate = -8  ### condition: 'x_coordinate': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
y_coordinate = 6  ### condition: 'y_coordinate': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the distance from the origin using the Pythagorean theorem
distance = (x_coordinate**2 + y_coordinate**2)**0.5  ### condition: 'distance': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the distance from the origin to the point
print(f"Distance from the origin to the point (-8, 6): {distance}")