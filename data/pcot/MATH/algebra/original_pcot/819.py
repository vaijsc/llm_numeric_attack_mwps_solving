# Define the midpoint coordinates
midpoint_x = 3  ### condition: 'midpoint_x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
midpoint_y = -2  ### condition: 'midpoint_y': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the x-coordinate of the known endpoint
endpoint1_x = 1  ### condition: 'endpoint1_x': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the y-coordinate of the known endpoint
endpoint1_y = 6  ### condition: 'endpoint1_y': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the x-coordinate of the other endpoint
endpoint2_x = 2 * midpoint_x - endpoint1_x  ### condition: 'endpoint2_x': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the y-coordinate of the other endpoint
endpoint2_y = 2 * midpoint_y - endpoint1_y  ### condition: 'endpoint2_y': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the coordinates of the other endpoint
print(f"The other endpoint is: ({endpoint2_x}, {endpoint2_y})")