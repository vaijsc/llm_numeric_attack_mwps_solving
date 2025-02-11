# Define the value under the square root for the first term
value_1 = 27  ### condition: 'value_1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the square root of the first value
sqrt_value_1 = value_1 ** 0.5  ### condition: 'sqrt_value_1': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the ceiling of the square root of the first value
ceiling_value_1 = int(sqrt_value_1) + (1 if sqrt_value_1 % 1 > 0 else 0)  ### condition: 'ceiling_value_1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the value under the square root for the second term
value_2 = 26  ### condition: 'value_2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the square root of the second value
sqrt_value_2 = value_2 ** 0.5  ### condition: 'sqrt_value_2': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the floor of the square root of the second value
floor_value_2 = int(sqrt_value_2)  ### condition: 'floor_value_2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the final result by subtracting floor_value_2 from ceiling_value_1
result = ceiling_value_1 - floor_value_2  ### condition: 'result': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"The result of the expression is: {result}")