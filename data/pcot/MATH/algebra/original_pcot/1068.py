# Define the slope of the given line
slope = 4  ### condition: 'slope': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the x-coordinate of the point the new line passes through
x_coordinate = 5  ### condition: 'x_coordinate': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the y-coordinate of the point the new line passes through
y_coordinate = 10  ### condition: 'y_coordinate': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the y-intercept of the new line using the point-slope form
y_intercept = y_coordinate - (slope * x_coordinate)  ### condition: 'y_intercept': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the y-coordinate where the line crosses the y-axis
print(f"The y-coordinate where the line crosses the y-axis: {y_intercept}")