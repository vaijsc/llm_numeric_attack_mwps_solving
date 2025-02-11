# Define the base value
base_value = 19  ### condition: 'base_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the square of the base value
square_value = base_value ** 2  ### condition: 'square_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate twice the base value
double_value = 2 * base_value  ### condition: 'double_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the final value by adding the square and double value plus 1
final_value = square_value + double_value + 1  ### condition: 'final_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"The value of $19^2 + 2(19) + 1$ is: {final_value}")