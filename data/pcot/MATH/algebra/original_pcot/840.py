# Define the cost of three pencils and one jumbo eraser in cents
cost_three_pencils_and_eraser = 124  ### condition: 'cost_three_pencils_and_eraser': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the cost of five pencils and one jumbo eraser in cents
cost_five_pencils_and_eraser = 182  ### condition: 'cost_five_pencils_and_eraser': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the cost difference between the two scenarios in cents
cost_difference = cost_five_pencils_and_eraser - cost_three_pencils_and_eraser  ### condition: 'cost_difference': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the number of extra pencils in the second scenario
extra_pencils = 5 - 3  ### condition: 'extra_pencils': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Assert that we can perfectly divide the cost difference by the number of extra pencils
assert cost_difference % extra_pencils == 0, "The division has a remainder, which is not allowed for this problem."
# Calculate the cost of one pencil in cents
cost_of_one_pencil = cost_difference // extra_pencils  ### condition: 'cost_of_one_pencil': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the cost of one pencil in cents
print(f"The cost of a pencil is: {cost_of_one_pencil} cents")