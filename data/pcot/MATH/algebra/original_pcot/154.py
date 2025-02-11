# Define the ratio of x to y
ratio_x_to_y = 2  ### condition: 'ratio_x_to_y': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the ratio of z to x
ratio_z_to_x = 4  ### condition: 'ratio_z_to_x': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the ratio of z to y using the relationships
ratio_z_to_y = ratio_z_to_x * ratio_x_to_y  ### condition: 'ratio_z_to_y': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of z to y
print(f"The value of z/y is: {ratio_z_to_y}")