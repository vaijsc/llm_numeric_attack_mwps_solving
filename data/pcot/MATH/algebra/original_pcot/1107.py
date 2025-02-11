# Define the numerator of the right side of the equation
right_numerator = 1  ### condition: 'right_numerator': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the denominator of the left side of the equation
left_denominator = 1  ### condition: 'left_denominator': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Set the expressions for A and B based on the equation
A = right_numerator  ### condition: 'A': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
B = -right_numerator  ### condition: 'B': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate A-B
result = A - B  ### condition: 'result': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the result
print(f"A - B = {result}")