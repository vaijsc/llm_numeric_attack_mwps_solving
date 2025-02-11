# Define the value of B
B = 2  ### condition: 'B': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the result of the operation
result = 19  ### condition: 'result': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate A using the defined operation A ♥ B
A = result - B - 4  ### condition: 'A': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of A
print(f"The value of A is: {A}")