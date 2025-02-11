# Define the total number of quarters
total_quarters = 20  ### condition: 'total_quarters': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the number of quarters in the second pile
# Let second_pile = x, then we have:
# first_pile = x - 3, third_pile = x - 2, fourth_pile = 2 * x
# Hence, total_quarters = (x - 3) + x + (x - 2) + (2 * x)
# This simplifies to 5x - 5 = total_quarters
assert (total_quarters + 5) % 5 == 0, "The division has a remainder, which is not allowed for this problem."
second_pile = (total_quarters + 5) // 5  ### condition: 'second_pile': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the number of quarters in the first pile
first_pile = second_pile - 3  ### condition: 'first_pile': {'type': 'int', '<=': 'second_pile', '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the number of quarters in the third pile
third_pile = second_pile - 2  ### condition: 'third_pile': {'type': 'int', '<=': 'second_pile', '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the number of quarters in the fourth pile
fourth_pile = 2 * second_pile  ### condition: 'fourth_pile': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the number of quarters in the fourth pile
print(f"Number of quarters in the fourth pile: {fourth_pile}")