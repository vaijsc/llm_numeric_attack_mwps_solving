# Define the sum of the three consecutive even integers
sum_of_integers = 66  ### condition: 'sum_of_integers': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the first even integer as 'x'
first_integer = 0  ### condition: 'first_integer': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the second even integer as 'x + 2'
second_integer = first_integer + 2  ### condition: 'second_integer': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the third even integer as 'x + 4'
third_integer = first_integer + 4  ### condition: 'third_integer': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the sum of three consecutive even integers
consecutive_integers_sum = first_integer + second_integer + third_integer  ### condition: 'consecutive_integers_sum': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Assert that the sum of the integers is equal to the given sum
assert consecutive_integers_sum == sum_of_integers, "The sum does not match the given total."
# Calculate the smallest even integer
first_integer = (sum_of_integers - 6) // 3  ### condition: 'first_integer': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the smallest of the three integers
print(f"The smallest of the three consecutive even integers is: {first_integer}")