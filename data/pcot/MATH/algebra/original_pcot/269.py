# Define the coordinates of the first endpoint
x1 = -4  ### condition: 'x1': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
y1 = 1   ### condition: 'y1': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the coordinates of the second endpoint
x2 = 1   ### condition: 'x2': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
y2 = 13  ### condition: 'y2': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the difference in x coordinates
delta_x = x2 - x1  ### condition: 'delta_x': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the difference in y coordinates
delta_y = y2 - y1  ### condition: 'delta_y': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the length of the segment using the distance formula
length_segment = (delta_x ** 2 + delta_y ** 2) ** 0.5  ### condition: 'length_segment': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the length of the segment
print(f"The length of the segment is: {length_segment}")