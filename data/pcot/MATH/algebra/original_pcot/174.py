# Define the equation coefficients
a = 5  ### condition: 'a': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
b = -20  ### condition: 'b': {'type': 'int', '<=': None, '>=': -20, 'science_constant': False, 'direct_from_question': True}
c = 18  ### condition: 'c': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the discriminant
discriminant = b**2 - 4*a*c  ### condition: 'discriminant': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Assert that the discriminant is non-negative
assert discriminant >= 0, "Discriminant must be non-negative for real solutions."
# Calculate the two solutions using the quadratic formula
solution1 = (-b + discriminant**0.5) / (2*a)  ### condition: 'solution1': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
solution2 = (-b - discriminant**0.5) / (2*a)  ### condition: 'solution2': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Round the solutions to the nearest integer
rounded_solution1 = round(solution1)  ### condition: 'rounded_solution1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
rounded_solution2 = round(solution2)  ### condition: 'rounded_solution2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the result of multiplying the two rounded solutions
result = rounded_solution1 * rounded_solution2  ### condition: 'result': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the result
print(f"The result of multiplying the two rounded solutions is: {result}")