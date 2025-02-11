# Define Monica's height in feet
monica_height = 5  ### condition: 'monica_height': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the length of Monica's shadow in feet
monica_shadow_length = 2  ### condition: 'monica_shadow_length': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the length of the pine tree's shadow in feet
pine_tree_shadow_length = 34  ### condition: 'pine_tree_shadow_length': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the height of the pine tree using the ratio of heights and shadow lengths
pine_tree_height = (monica_height / monica_shadow_length) * pine_tree_shadow_length  ### condition: 'pine_tree_height': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Convert the pine tree height to int
pine_tree_height = int(pine_tree_height) ### condition: 'pine_tree_height': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the height of the pine tree
print(f"The height of the pine tree is: {pine_tree_height} feet")