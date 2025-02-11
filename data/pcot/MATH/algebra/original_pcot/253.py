# Define the first number P
P = 3  ### condition: 'P': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the second number Q
Q = 6  ### condition: 'Q': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the third number R
R = 8  ### condition: 'R': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the value of the operation Q * R
Q_star_R = (Q + R) / 2  ### condition: 'Q_star_R': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the final value of P * (Q * R)
result = (P + Q_star_R) / 2  ### condition: 'result': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"The value of 3 * (6 * 8) is: {result}")