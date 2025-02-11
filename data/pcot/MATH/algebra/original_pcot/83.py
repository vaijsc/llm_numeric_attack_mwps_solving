# Define the amount of salt used in teaspoons
salt_used = 2  ### condition: 'salt_used': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the amount of salt needed per quart of water in teaspoons
salt_per_quart = 0.25  ### condition: 'salt_per_quart': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the number of quarts of water based on the amount of salt used
quarts_of_water = salt_used / salt_per_quart  ### condition: 'quarts_of_water': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the number of quarts of water that will be used
print(f"Quarts of water used for two teaspoons of salt: {quarts_of_water}")