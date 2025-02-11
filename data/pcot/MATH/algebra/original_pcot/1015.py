# Define the coefficients of the quadratic equation
a = 1  ### condition: 'a': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
b = -5  ### condition: 'b': {'type': 'int', '<=': None, '>=': -5, 'science_constant': False, 'direct_from_question': True}
c = -14  ### condition: 'c': {'type': 'int', '<=': None, '>=': -14, 'science_constant': False, 'direct_from_question': True}
# Calculate the discriminant of the quadratic equation
discriminant = b**2 - 4*a*c  ### condition: 'discriminant': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Assert that the discriminant is non-negative
assert discriminant >= 0, "The discriminant must be non-negative."
# Calculate the two roots of the quadratic equation
root1 = (-b + discriminant**0.5) / (2*a)  ### condition: 'root1': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
root2 = (-b - discriminant**0.5) / (2*a)  ### condition: 'root2': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Find the smallest integer value of n such that n^2 - 5n - 14 < 0
n = int(root2) + 1  ### condition: 'n': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the smallest integer value of n
print(f"The smallest integer value of n such that n^2 - 5n - 14 is negative: {n}")