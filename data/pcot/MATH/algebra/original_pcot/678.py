# Define the value of 19
value_19 = 19  ### condition: 'value_19': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the value of 31
value_31 = 31  ### condition: 'value_31': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate 19 squared
square_19 = value_19 ** 2  ### condition: 'square_19': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate 31 squared
square_31 = value_31 ** 2  ### condition: 'square_31': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate how much greater 31 squared is than 19 squared
difference = square_31 - square_19  ### condition: 'difference': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the difference
print(f"The value of 31^2 is greater than 19^2 by: {difference}")