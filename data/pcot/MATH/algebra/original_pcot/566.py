# Define the variable x in the equation
x = 0  ### condition: 'x': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Rearranging the equation to standard form: x^2 + 10x + 10x + 100 = 0
# Coefficient of x^2
a = 1  ### condition: 'a': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Coefficient of x
b = 20  ### condition: 'b': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Constant term
c = 100  ### condition: 'c': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the discriminant
discriminant = b**2 - 4*a*c  ### condition: 'discriminant': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the two solutions using the quadratic formula
solution1 = (-b + discriminant**0.5) / (2 * a)  ### condition: 'solution1': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
solution2 = (-b - discriminant**0.5) / (2 * a)  ### condition: 'solution2': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the solutions
print(f"Solutions are: x1 = {solution1}, x2 = {solution2}")