# Define the 7th term of the arithmetic sequence
seventh_term = 30  ### condition: 'seventh_term': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the 11th term of the arithmetic sequence
eleventh_term = 60  ### condition: 'eleventh_term': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the common difference (d) of the arithmetic sequence
# The difference between the term numbers is 11 - 7 = 4, hence we find d
difference_in_terms = 4  ### condition: 'difference_in_terms': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the common difference
common_difference = (eleventh_term - seventh_term) / difference_in_terms  ### condition: 'common_difference': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the term number for which we want to find the value
term_number = 21  ### condition: 'term_number': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the index of the first term
first_term_index = 7  ### condition: 'first_term_index': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the number of steps from the 7th term to the 21st term
steps = term_number - first_term_index  ### condition: 'steps': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the 21st term of the arithmetic sequence
twenty_first_term = seventh_term + steps * common_difference  ### condition: 'twenty_first_term': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the 21st term of the arithmetic sequence
print(f"The 21st term of the sequence is: {twenty_first_term}")