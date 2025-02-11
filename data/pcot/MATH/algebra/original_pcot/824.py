# Define the value to be squared
value = 115  ### condition: 'value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the square of the value
squared_value = value ** 2  ### condition: 'squared_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the squared value
print(f"The square of {value} is: {squared_value}")