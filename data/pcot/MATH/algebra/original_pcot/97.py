# Define the first term of the arithmetic sequence
first_term = 13  ### condition: 'first_term': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the common difference of the arithmetic sequence
common_difference = 7  ### condition: 'common_difference': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the last term of the arithmetic sequence
last_term = 2008  ### condition: 'last_term': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the number of terms in the arithmetic sequence using the formula for the nth term
# n = (last_term - first_term) / common_difference + 1
# Assert that the numerator is divisible by the common difference
assert (last_term - first_term) % common_difference == 0, "The division has a remainder, which is not allowed for this problem."
# Calculate the number of integers in the arithmetic sequence
number_of_terms = (last_term - first_term) // common_difference + 1  ### condition: 'number_of_terms': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the number of integers in the arithmetic sequence
print(f"Number of integers in the arithmetic sequence: {number_of_terms}")