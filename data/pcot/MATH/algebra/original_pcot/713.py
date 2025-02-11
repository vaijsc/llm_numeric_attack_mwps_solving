# Define the sum of the three consecutive integers
total_sum = 27  ### condition: 'total_sum': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the number of consecutive integers
num_consecutive = 3  ### condition: 'num_consecutive': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
# Calculate the average of the three integers
average = total_sum // num_consecutive  ### condition: 'average': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Assert that the division will not produce a remainder
assert total_sum % num_consecutive == 0, "The sum of the integers does not evenly divide."
# Define the first consecutive integer
first_integer = average - 1  ### condition: 'first_integer': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the second consecutive integer
second_integer = average  ### condition: 'second_integer': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the third consecutive integer
third_integer = average + 1  ### condition: 'third_integer': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the product of the three consecutive integers
product_of_integers = first_integer * second_integer * third_integer  ### condition: 'product_of_integers': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the product of the integers
print(f"The product of the integers is: {product_of_integers}")