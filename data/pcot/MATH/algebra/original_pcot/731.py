# Define the first part of the expression (7 + 5)
first_part = 7 + 5  ### condition: 'first_part': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the second part of the expression (7 - 5)
second_part = 7 - 5  ### condition: 'second_part': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate (7 + 5) squared
first_part_squared = first_part ** 2  ### condition: 'first_part_squared': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate (7 - 5) squared
second_part_squared = second_part ** 2  ### condition: 'second_part_squared': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the final result by subtracting the two squared values
result = first_part_squared - second_part_squared  ### condition: 'result': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"The value of (7 + 5)^2 - (7 - 5)^2 is: {result}")