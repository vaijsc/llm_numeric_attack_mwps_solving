# Define the value of the first number
a = 102  ### condition: 'a': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the value of the second number
b = 98   ### condition: 'b': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the square of the first number
a_squared = a ** 2  ### condition: 'a_squared': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the square of the second number
b_squared = b ** 2  ### condition: 'b_squared': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the difference between the squares
difference = a_squared - b_squared  ### condition: 'difference': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the result of the evaluation
print(f"Result of $102^2 - 98^2$: {difference}")