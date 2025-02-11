# Define the sum of the groom's and bride's ages
total_age = 51  ### condition: 'total_age': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the difference to account for the groom's age relation to the bride's age
groom_age_difference = 15  ### condition: 'groom_age_difference': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the variable for the bride's age
bride_current_age = 0  ### condition: 'bride_current_age': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the groom's age using the relationship given in the problem
# Let groom's age = G and bride's age = B
# According to the problem: G = 15 + (1/2)B and G + B = 51
# Substituting for G: (15 + (1/2)B) + B = 51
# This simplifies to: 15 + (3/2)B = 51 --> (3/2)B = 36
# Therefore, B = 36 * (2/3) = 24
bride_current_age = (total_age - groom_age_difference) * (2/3)  ### condition: 'bride_current_age': {'type': 'float', '<=': 'total_age', '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Now calculating groom's current age
groom_current_age = total_age - bride_current_age  ### condition: 'groom_current_age': {'type': 'float', '<=': 'total_age', '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Assert that the groom's age derived using the relationship is correct
assert groom_current_age == (0.5 * bride_current_age + groom_age_difference), "The groom's age does not match the given relationship."
# Print the groom's current age
print(f"The groom's current age is: {int(groom_current_age)}")