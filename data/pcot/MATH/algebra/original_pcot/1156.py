# Define the coordinates of the first endpoint
x1 = -3  ### condition: 'x1': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
y1 = 7   ### condition: 'y1': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the coordinates of the second endpoint
x2 = 2   ### condition: 'x2': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
y2 = -5  ### condition: 'y2': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the difference in x-coordinates
delta_x = x2 - x1  ### condition: 'delta_x': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the difference in y-coordinates
delta_y = y2 - y1  ### condition: 'delta_y': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the length of the line segment using the distance formula
length = (delta_x ** 2 + delta_y ** 2) ** 0.5  ### condition: 'length': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the length of the line segment
print(f"The length of the line segment is: {length}")