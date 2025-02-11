# Define the coefficients of the quadratic equation
a = 2  ### condition: 'a': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
b = 4  ### condition: 'b': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
c = -1  ### condition: 'c': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the discriminant
discriminant = b**2 - 4*a*c  ### condition: 'discriminant': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the solutions using the quadratic formula
solution1 = (-b + (discriminant**0.5)) / (2*a)  ### condition: 'solution1': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
solution2 = (-b - (discriminant**0.5)) / (2*a)  ### condition: 'solution2': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the sum of the squares of the solutions
sum_of_squares = solution1**2 + solution2**2  ### condition: 'sum_of_squares': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the sum of the squares of the solutions
print(f"The sum of the squares of the solutions is: {sum_of_squares}")