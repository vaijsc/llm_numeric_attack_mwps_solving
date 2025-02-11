# Define the first integer K
K = 6  ### condition: 'K': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the second integer L
L = 5  ### condition: 'L': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate K + L
sum_KL = K + L  ### condition: 'sum_KL': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate K - L
difference_KL = K - L  ### condition: 'difference_KL': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the operation K star L
result = sum_KL * difference_KL  ### condition: 'result': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the result of the operation
print(f"The value of 6 star 5 is: {result}")