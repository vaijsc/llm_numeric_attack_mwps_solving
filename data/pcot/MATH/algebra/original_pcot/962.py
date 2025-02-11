# Define the area of the base of the cone
base_area = 30.0  ### condition: 'base_area': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the height of the cone
height = 6.5  ### condition: 'height': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the volume of the cone using the formula V = (1/3) * B * h
volume = (1/3) * base_area * height  ### condition: 'volume': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the volume of the cone
print(f"The volume of the cone is: {volume} cubic units")