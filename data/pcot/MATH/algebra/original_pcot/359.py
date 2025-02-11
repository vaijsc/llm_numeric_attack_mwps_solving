# Define the lower bound of the integer range
lower_bound = -30  ### condition: 'lower_bound': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the upper bound of the integer range
upper_bound = 26  ### condition: 'upper_bound': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the number of terms in the range
number_of_terms = upper_bound - lower_bound + 1  ### condition: 'number_of_terms': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the sum of the integers using the formula for the sum of an arithmetic series
sum_of_integers = (number_of_terms * (lower_bound + upper_bound)) // 2  ### condition: 'sum_of_integers': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the sum of all integers in the range
print(f"The sum of all integers x for which -30 ≤ x ≤ 26 is: {sum_of_integers}")