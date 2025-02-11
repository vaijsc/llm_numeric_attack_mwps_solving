# Define the value for x
x1 = 6  ### condition: 'x1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
x2 = 4  ### condition: 'x2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate f(6)
f_x1 = (x1 - 1) * (x1 - 3) * (x1 - 7) * (x1 - 9)  ### condition: 'f_x1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate f(4)
f_x2 = (x2 - 1) * (x2 - 3) * (x2 - 7) * (x2 - 9)  ### condition: 'f_x2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the difference f(6) - f(4)
result = f_x1 - f_x2  ### condition: 'result': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"f(6) - f(4) = {result}")