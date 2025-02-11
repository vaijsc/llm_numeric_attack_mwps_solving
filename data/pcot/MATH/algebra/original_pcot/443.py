# Define the value of the square root of 400
sqrt_400 = 400 ** 0.5  ### condition: 'sqrt_400': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the value of the square root of 81
sqrt_81 = 81 ** 0.5  ### condition: 'sqrt_81': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the value of n using the equation sqrt_400 = sqrt_81 + sqrt(n)
n = (sqrt_400 - sqrt_81) ** 2  ### condition: 'n': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of n
print(f"The value of n is: {n}")