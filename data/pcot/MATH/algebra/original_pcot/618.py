# Define the total number of heads counted
total_heads = 10  ### condition: 'total_heads': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the total number of legs counted
total_legs = 30  ### condition: 'total_legs': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the number of legs per clown and per horse
legs_per_clown = 2  ### condition: 'legs_per_clown': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
legs_per_horse = 4  ### condition: 'legs_per_horse': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the number of clowns and horses
# Let c be the number of clowns, and h be the number of horses
# Set up the equations based on the heads and legs counted:
# 1. c + h = total_heads
# 2. 2c + 4h = total_legs
# From the first equation, we have c = total_heads - h
# Substitute into the second equation:
# 2(total_heads - h) + 4h = total_legs
# which simplifies to: 2*total_heads + 2h = total_legs
# Solving for h gives us: h = (total_legs - 2*total_heads) / 2
# Assert that the calculation will not produce a remainder
assert (total_legs - 2 * total_heads) % 2 == 0, "The calculation has a remainder, which is not allowed for this problem."
# Calculate the number of horses
number_of_horses = (total_legs - 2 * total_heads) // 2  ### condition: 'number_of_horses': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the number of horses seen in the parade
print(f"Number of horses seen in the parade: {number_of_horses}")