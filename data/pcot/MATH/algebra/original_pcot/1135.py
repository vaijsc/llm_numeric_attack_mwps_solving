# Define the coefficients of the quadratic inequality
a = 6  ### condition: 'a': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
b = 1  ### condition: 'b': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
c = -2  ### condition: 'c': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the discriminant of the quadratic equation
discriminant = b**2 - 4 * a * c  ### condition: 'discriminant': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the roots using the quadratic formula
root1 = (-b + discriminant**0.5) / (2 * a)  ### condition: 'root1': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
root2 = (-b - discriminant**0.5) / (2 * a)  ### condition: 'root2': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Determine the maximum integer value of x that satisfies the inequality
max_x = int(root1) if root1 > root2 else int(root2)  ### condition: 'max_x': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the greatest integer value of x for which the inequality holds
print(f"The greatest integer value of x for which 6x^2 + x - 2 < 0 is: {max_x}")