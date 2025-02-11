# Define the last number in the series
last_number = 100  ### condition: 'last_number': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
# Calculate the sum of the series using the formula n(n + 1) / 2
# Assert that the last_number is a positive integer
assert last_number > 0, "The last number must be greater than 0."
# Calculate the sum using the formula
total_sum = (last_number * (last_number + 1)) // 2  ### condition: 'total_sum': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the total sum
print(f"The sum of the series 1 + 2 + 3 + ... + {last_number} is: {total_sum}")