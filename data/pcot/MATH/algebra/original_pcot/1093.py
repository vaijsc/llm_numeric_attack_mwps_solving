# Define the value of 10
value = 10  ### condition: 'value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the square root of the value
sqrt_value = value ** 0.5  ### condition: 'sqrt_value': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the ceiling of the square root
ceil_sqrt = int(sqrt_value) + (1 if sqrt_value % 1 > 0 else 0)  ### condition: 'ceil_sqrt': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the floor of the square root
floor_sqrt = int(sqrt_value)  ### condition: 'floor_sqrt': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the final result
result = ceil_sqrt + floor_sqrt  ### condition: 'result': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"The result of the expression is: {result}")