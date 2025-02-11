# Define Robert's coordinates
robert_x = 4  ### condition: 'robert_x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
robert_y = 3  ### condition: 'robert_y': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define Lucy's coordinates
lucy_x = 6  ### condition: 'lucy_x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
lucy_y = 1  ### condition: 'lucy_y': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define Liz's coordinates
liz_x = 1  ### condition: 'liz_x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
liz_y = 7  ### condition: 'liz_y': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the distance from Robert to Lucy
distance_robert_lucy = ((lucy_x - robert_x) ** 2 + (lucy_y - robert_y) ** 2) ** 0.5  ### condition: 'distance_robert_lucy': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the distance from Robert to Liz
distance_robert_liz = ((liz_x - robert_x) ** 2 + (liz_y - robert_y) ** 2) ** 0.5  ### condition: 'distance_robert_liz': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Determine the farther distance
farther_distance = max(distance_robert_lucy, distance_robert_liz)  ### condition: 'farther_distance': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the farther distance
print(f"The farther person from Robert is {farther_distance:.2f} units away.")