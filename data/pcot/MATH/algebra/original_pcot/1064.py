# Define the sum of the consecutive integers
sum_of_integers = 22  ### condition: 'sum_of_integers': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the number of integers in the set
number_of_integers = 4  ### condition: 'number_of_integers': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the average of the consecutive integers
average_of_integers = sum_of_integers / number_of_integers  ### condition: 'average_of_integers': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the first integer of the set
first_integer = average_of_integers - (number_of_integers - 1) / 2  ### condition: 'first_integer': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Assert that first_integer is an integer (since it represents an integer value)
assert first_integer % 1 == 0, "First integer is not a whole number, which is not allowed for this problem."
# Convert first_integer to an integer
first_integer = int(first_integer)  ### condition: 'first_integer': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the sum of the new set of integers increased by 2
new_sum_of_integers = (first_integer + 2) + (first_integer + 1 + 2) + (first_integer + 2 + 2) + (first_integer + 3 + 2)  ### condition: 'new_sum_of_integers': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Multiply by 20
final_sum = new_sum_of_integers * 20  ### condition: 'final_sum': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the final sum
print(f"The sum of the new set of integers is: {final_sum}")