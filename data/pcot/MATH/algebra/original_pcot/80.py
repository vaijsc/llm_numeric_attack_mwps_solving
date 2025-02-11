# Define the lower and upper bounds of the range
lower_bound = 100  ### condition: 'lower_bound': {'type': 'int', '<=': 200, '>=': 0, 'science_constant': False, 'direct_from_question': True}
upper_bound = 200  ### condition: 'upper_bound': {'type': 'int', '<=': None, '>=': 'lower_bound', 'science_constant': False, 'direct_from_question': True}
# Calculate the first multiple of 3 greater than or equal to the lower bound
first_multiple_of_3 = lower_bound + (3 - lower_bound % 3) % 3  ### condition: 'first_multiple_of_3': {'type': 'int', '<=': 'upper_bound', '>=': 'lower_bound', 'science_constant': False, 'direct_from_question': False}
# Calculate the last multiple of 3 less than or equal to the upper bound
last_multiple_of_3 = upper_bound - (upper_bound % 3)  ### condition: 'last_multiple_of_3': {'type': 'int', '<=': 'upper_bound', '>=': 'lower_bound', 'science_constant': False, 'direct_from_question': False}
# Calculate the number of multiples of 3 in the range
number_of_multiples = (last_multiple_of_3 - first_multiple_of_3) // 3 + 1  ### condition: 'number_of_multiples': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the sum of all multiples of 3 in the range using the formula for the sum of an arithmetic series
sum_of_multiples = number_of_multiples * (first_multiple_of_3 + last_multiple_of_3) // 2  ### condition: 'sum_of_multiples': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the sum of all multiples of 3 between 100 and 200
print(f"The sum of all multiples of 3 between 100 and 200 is: {sum_of_multiples}")