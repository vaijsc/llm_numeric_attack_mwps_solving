# Define the coordinates of the first endpoint
x1 = 1  ### condition: 'x1': {'type': 'int', '<=': None, '>=': -float('inf'), 'science_constant': False, 'direct_from_question': True}
y1 = 2  ### condition: 'y1': {'type': 'int', '<=': None, '>=': -float('inf'), 'science_constant': False, 'direct_from_question': True}
# Define the coordinates of the second endpoint
x2 = -4  ### condition: 'x2': {'type': 'int', '<=': None, '>=': -float('inf'), 'science_constant': False, 'direct_from_question': True}
y2 = -10  ### condition: 'y2': {'type': 'int', '<=': None, '>=': -float('inf'), 'science_constant': False, 'direct_from_question': True}
# Calculate the difference in x and y coordinates
delta_x = x2 - x1  ### condition: 'delta_x': {'type': 'int', '<=': None, '>=': -float('inf'), 'science_constant': False, 'direct_from_question': False}
delta_y = y2 - y1  ### condition: 'delta_y': {'type': 'int', '<=': None, '>=': -float('inf'), 'science_constant': False, 'direct_from_question': False}
# Calculate the square of the differences
square_delta_x = delta_x ** 2  ### condition: 'square_delta_x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
square_delta_y = delta_y ** 2  ### condition: 'square_delta_y': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the distance using the distance formula
distance = (square_delta_x + square_delta_y) ** 0.5  ### condition: 'distance': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the length of the segment
print(f"Length of the segment: {distance}")