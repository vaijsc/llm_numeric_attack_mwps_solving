# Define the total sum of the 27 consecutive integers
total_sum = 3**7  ### condition: 'total_sum': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the number of consecutive integers
number_of_integers = 27  ### condition: 'number_of_integers': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
# Calculate the mean (sum divided by count) to find the median
# Assert that the division will not produce a remainder
assert total_sum % number_of_integers == 0, "The division has a remainder, which is not allowed for this problem."
# Calculate the median of the consecutive integers
median = total_sum // number_of_integers  ### condition: 'median': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the median of the 27 consecutive positive integers
print(f"The median of the 27 consecutive positive integers is: {median}")