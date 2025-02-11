# Define the arithmetic mean of A, B, and C
mean_value = 10  ### condition: 'mean_value': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the relationship between A and B
A_minus_B = -6  ### condition: 'A_minus_B': {'type': 'int', '<=': None, '>=': -6, 'science_constant': False, 'direct_from_question': True}
# Define the relationship between C and B
C_minus_B = 3  ### condition: 'C_minus_B': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the sum of A, B, and C using the mean
total_sum = mean_value * 3  ### condition: 'total_sum': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Express A and C in terms of B
# A = B + (A_minus_B)
# C = B + (C_minus_B)
# Now we can rewrite total_sum as follows:
# total_sum = A + B + C = (B + (A_minus_B)) + B + (B + (C_minus_B))
# total_sum = 3B + (A_minus_B + C_minus_B)
# Calculate the values of B
B_value = (total_sum - (A_minus_B + C_minus_B)) / 3  ### condition: 'B_value': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the value of C
C_value = B_value + C_minus_B  ### condition: 'C_value': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of C
print(f"The value of C is: {C_value}")