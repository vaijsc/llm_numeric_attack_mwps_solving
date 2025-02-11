# Define the weight of the cake for which flour is provided
weight_of_cake = 2  ### condition: 'weight_of_cake': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the amount of flour required for the cake weight of 2 pounds
flour_for_two_pounds = 1.5  ### condition: 'flour_for_two_pounds': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the weight of each cake for the intended recipe
target_weight_per_cake = 5  ### condition: 'target_weight_per_cake': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the number of cakes to prepare
number_of_cakes = 2  ### condition: 'number_of_cakes': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the total weight of all cakes to be prepared
total_weight_of_cakes = target_weight_per_cake * number_of_cakes  ### condition: 'total_weight_of_cakes': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the ratio of the recipe weight to the total weight
ratio = total_weight_of_cakes / weight_of_cake  ### condition: 'ratio': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the total amount of flour needed for the desired cakes
total_flour_needed = flour_for_two_pounds * ratio  ### condition: 'total_flour_needed': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the total amount of flour needed
print(f"Total cups of flour needed for 2 five-pound cakes: {total_flour_needed}")