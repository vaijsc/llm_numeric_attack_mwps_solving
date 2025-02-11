# Define the first term of the sequence
first_term = 2222  ### condition: 'first_term': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the difference between successive terms
difference = 1010  ### condition: 'difference': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the sixth term
sixth_term = first_term + (5 * difference)  ### condition: 'sixth_term': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the seventh term
seventh_term = first_term + (6 * difference)  ### condition: 'seventh_term': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the sum of the sixth and seventh terms
sum_sixth_and_seventh = sixth_term + seventh_term  ### condition: 'sum_sixth_and_seventh': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the sum of the sixth and seventh terms
print(f"The sum of the sixth and seventh terms: {sum_sixth_and_seventh}")