# Given problem: If $2ab = 12$, evaluate $8a^2b^2$.
# Define the equation given in the problem
two_ab = 12  ### condition: 'two_ab': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the value of ab by rearranging the equation
ab = two_ab / 2  ### condition: 'ab': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the value of a^2b^2 using the formula (ab)^2
a_squared_b_squared = ab ** 2  ### condition: 'a_squared_b_squared': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the final value of 8a^2b^2
final_value = 8 * a_squared_b_squared  ### condition: 'final_value': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the final evaluated value
print(f"The value of 8a^2b^2 is: {final_value}")