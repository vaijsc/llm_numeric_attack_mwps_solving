# Define the sum of the seven consecutive integers
total_sum = 49  ### condition: 'total_sum': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the number of consecutive integers
num_integers = 7  ### condition: 'num_integers': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
# Calculate the average of the integers
average = total_sum / num_integers  ### condition: 'average': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Since the integers are consecutive, the smallest integer can be calculated
smallest_integer = average - (num_integers - 1) / 2  ### condition: 'smallest_integer': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Assert that the smallest_integer is an integer
assert smallest_integer % 1 == 0, "The smallest_integer calculation has to yield an integer."
# Convert to integer type
smallest_integer = int(smallest_integer)  ### condition: 'smallest_integer': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the smallest of the seven integers
print(f"The smallest of the seven consecutive integers is: {smallest_integer}")