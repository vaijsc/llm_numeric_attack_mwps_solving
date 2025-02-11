# Define the third term of the arithmetic sequence
third_term = 5  ### condition: 'third_term': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the sixth term of the arithmetic sequence
sixth_term = -1  ### condition: 'sixth_term': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the positions of the terms
third_position = 3  ### condition: 'third_position': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
sixth_position = 6  ### condition: 'sixth_position': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the common difference using the term positions and their values
common_difference = (sixth_term - third_term) / (sixth_position - third_position)  ### condition: 'common_difference': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the first term using the third term and the common difference
first_term = third_term - (third_position - 1) * common_difference  ### condition: 'first_term': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Define the position of the term we want to find (twelfth term)
twelfth_position = 12  ### condition: 'twelfth_position': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the twelfth term of the arithmetic sequence
twelfth_term = first_term + (twelfth_position - 1) * common_difference  ### condition: 'twelfth_term': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the twelfth term of the arithmetic sequence
print(f"The twelfth term of the arithmetic sequence is: {twelfth_term}")