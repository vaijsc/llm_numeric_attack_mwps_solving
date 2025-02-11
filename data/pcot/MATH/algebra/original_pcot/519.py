# Define the value to calculate the square root
value_for_square_root = 1000000  ### condition: 'value_for_square_root': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the square root of the value
square_root_value = value_for_square_root ** 0.5  ### condition: 'square_root_value': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the cube root of the value
cube_root_value = value_for_square_root ** (1/3)  ### condition: 'cube_root_value': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the final result by subtracting the cube root from the square root
final_result = square_root_value - cube_root_value  ### condition: 'final_result': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"The value of √{value_for_square_root} - ∛{value_for_square_root} is: {final_result}")