# Define the value of n for which we need to evaluate the function
n = 10  ### condition: 'n': {'type': 'int', '<=': 15, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate f(n) = n^2 + n + 17
f_n = n**2 + n + 17  ### condition: 'f_n': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the value of n for the previous function evaluation
n_minus_1 = 9  ### condition: 'n_minus_1': {'type': 'int', '<=': 15, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate f(n-1) = (n-1)^2 + (n-1) + 17
f_n_minus_1 = n_minus_1**2 + n_minus_1 + 17  ### condition: 'f_n_minus_1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the difference f(n) - f(n-1)
difference = f_n - f_n_minus_1  ### condition: 'difference': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the result
print(f"The value of f(10) - f(9) is: {difference}")