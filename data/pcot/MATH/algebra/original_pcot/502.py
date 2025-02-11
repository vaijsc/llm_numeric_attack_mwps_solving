# Define the first term of the arithmetic series
first_term = 28  ### condition: 'first_term': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the last term of the arithmetic series
last_term = 86  ### condition: 'last_term': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the common difference of the arithmetic series
common_difference = 2  ### condition: 'common_difference': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the number of terms in the arithmetic series
number_of_terms = ((last_term - first_term) // common_difference) + 1  ### condition: 'number_of_terms': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': False}
# Calculate the sum of the arithmetic series using the formula: sum = n/2 * (first_term + last_term)
sum_of_series = (number_of_terms / 2) * (first_term + last_term)  ### condition: 'sum_of_series': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of the arithmetic series
print(f"The value of the arithmetic series is: {sum_of_series}")