# Define the first number
number_one = 513  ### condition: 'number_one': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the second number
number_two = 487  ### condition: 'number_two': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the difference of squares using the formula a^2 - b^2 = (a - b)(a + b)
difference_of_squares = (number_one - number_two) * (number_one + number_two)  ### condition: 'difference_of_squares': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the result
print(f"The value of {number_one}^2 - {number_two}^2 is: {difference_of_squares}")