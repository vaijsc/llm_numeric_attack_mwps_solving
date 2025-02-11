# Define the first number A
A = 3  ### condition: 'A': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the second number B
B = 5  ### condition: 'B': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate A & B using the defined operation
A_and_B = (A + B) / 2  ### condition: 'A_and_B': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the third number C
C = 8  ### condition: 'C': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate (A & B) & C
result = (A_and_B + C) / 2  ### condition: 'result': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"The value of (3 & 5) & 8 is: {result}")