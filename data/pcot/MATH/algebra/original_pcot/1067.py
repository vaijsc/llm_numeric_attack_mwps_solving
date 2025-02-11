# Define the value of 99
value = 99  ### condition: 'value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate 99 squared
value_squared = value ** 2  ### condition: 'value_squared': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the total by adding 99 and 1 to the squared value
total = value_squared + value + 1  ### condition: 'total': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"The result of 99^2 + 99 + 1 is: {total}")