# Define the radius of the first cone
radius_first_cone = 3  ### condition: 'radius_first_cone': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the height of the first cone
height_first_cone = 24  ### condition: 'height_first_cone': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the volume of the first cone using the formula V = (1/3) * π * r^2 * h
# Here, we will use π as a science constant
pi = 3.14  ### condition: 'pi': {'type': 'float', '<=': None, '>=': 0, 'science_constant': True, 'direct_from_question': True}
volume_first_cone = (1/3) * pi * (radius_first_cone ** 2) * height_first_cone  ### condition: 'volume_first_cone': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the radius of the second cone, which is 1/3 of the first cone's radius
radius_second_cone = radius_first_cone / 3  ### condition: 'radius_second_cone': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the height of the second cone using the same volume
# Since the volumes are equal, we can set up the equation: volume_first_cone = volume_second_cone
# volume_second_cone = (1/3) * π * (radius_second_cone ** 2) * height_second_cone
# Therefore, we rearranged it to find height_second_cone
height_second_cone = (3 * volume_first_cone) / (pi * (radius_second_cone ** 2))  ### condition: 'height_second_cone': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the height of the second cone
print(f"Height of the second cone: {height_second_cone}")