# Define the sum of the two numbers
total_sum = 25  ### condition: 'total_sum': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the difference of the two numbers
total_difference = 11  ### condition: 'total_difference': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the larger number using the formulas:
# Let X be the larger number and Y be the smaller number:
# X + Y = total_sum
# X - Y = total_difference
# Therefore, X = (total_sum + total_difference) / 2 and Y = (total_sum - total_difference) / 2
# We will calculate the larger number (X) first
# Assert that the sum and difference will produce even number for calculation
assert (total_sum + total_difference) % 2 == 0, "The calculation for the larger number must yield an integer."
assert (total_sum - total_difference) % 2 == 0, "The calculation for the smaller number must yield an integer."
# Calculate the larger number
larger_number = (total_sum + total_difference) // 2  ### condition: 'larger_number': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the larger of the two numbers
print(f"The larger of the two numbers is: {larger_number}")