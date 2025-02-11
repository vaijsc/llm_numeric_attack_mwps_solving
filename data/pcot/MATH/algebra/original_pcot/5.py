# Define the first term of the arithmetic sequence
first_term = 6  ### condition: 'first_term': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the common difference of the arithmetic sequence
common_difference = 4  ### condition: 'common_difference': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the term number to find
term_number = 100  ### condition: 'term_number': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
# Calculate the 100th term of the arithmetic sequence using the formula: a_n = first_term + (n - 1) * common_difference
n_th_term = first_term + (term_number - 1) * common_difference  ### condition: 'n_th_term': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the 100th term of the arithmetic sequence
print(f"The 100th term of the arithmetic sequence is: {n_th_term}")