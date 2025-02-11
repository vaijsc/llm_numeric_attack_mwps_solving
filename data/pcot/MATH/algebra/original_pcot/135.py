# Define the coefficients of the given line equation
slope = 3 / 7  ### condition: 'slope': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the point through which the parallel line passes
point_x = 7  ### condition: 'point_x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
point_y = 4  ### condition: 'point_y': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the y-intercept of the line using the point-slope form
y_intercept = point_y - (slope * point_x)  ### condition: 'y_intercept': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the x-coordinate of the point on the y-axis
x_coordinate = 0  ### condition: 'x_coordinate': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the value of K (y-coordinate when x is 0)
K = slope * x_coordinate + y_intercept  ### condition: 'K': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of K
print(f"The value of K is: {K}")