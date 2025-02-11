# Define the value of 255
value_a = 255  ### condition: 'value_a': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the value of 245
value_b = 245  ### condition: 'value_b': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the difference of squares using the formula a^2 - b^2 = (a - b)(a + b)
difference_of_squares = (value_a - value_b) * (value_a + value_b)  ### condition: 'difference_of_squares': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of the difference of squares
print(f"The value of $255^2 - 245^2$ is: {difference_of_squares}")