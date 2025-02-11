# Define the coefficients of the quadratic equation
a = 1  ### condition: 'a': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
b = -7  ### condition: 'b': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
c = 7  ### condition: 'c': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the y-value for the line
line_y = -3  ### condition: 'line_y': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Set the quadratic equation equal to the line's y-value to find x-intercepts
# This gives us the equation: x^2 - 7x + 7 = -3
# Rearranging this gives: x^2 - 7x + 10 = 0
c_rearranged = c - line_y  ### condition: 'c_rearranged': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the sum of the roots using the formula: -b/a
sum_of_x_coordinates = -b / a  ### condition: 'sum_of_x_coordinates': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the sum of the x-coordinates
print(f"The sum of the x-coordinates of the intersection points: {sum_of_x_coordinates}")