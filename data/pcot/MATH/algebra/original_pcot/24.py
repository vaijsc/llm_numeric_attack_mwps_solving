# Define the value of a
a = 5  ### condition: 'a': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate a raised to the power of 3
a_cubed = a ** 3  ### condition: 'a_cubed': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate a raised to the power of 2
a_squared = a ** 2  ### condition: 'a_squared': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the product of a_cubed and a_squared
result = a_cubed * a_squared  ### condition: 'result': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the result of the expression a^3 * a^2
print(f"The result of the expression a^3 * a^2 is: {result}")