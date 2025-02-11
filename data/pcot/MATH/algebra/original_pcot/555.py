# Define the coefficients of the quadratic equation
a = 1  ### condition: 'a': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
b = -5  ### condition: 'b': {'type': 'int', '<=': None, '>=': -5, 'science_constant': False, 'direct_from_question': True}
c = -36  ### condition: 'c': {'type': 'int', '<=': None, '>=': -36, 'science_constant': False, 'direct_from_question': True}
# Calculate the discriminant of the quadratic equation
discriminant = b ** 2 - 4 * a * c  ### condition: 'discriminant': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Assert that the discriminant is non-negative for real roots
assert discriminant >= 0, "The discriminant is negative, which means there are no real roots."
# Calculate the two possible values of x using the quadratic formula
x1 = (-b + discriminant ** 0.5) / (2 * a)  ### condition: 'x1': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
x2 = (-b - discriminant ** 0.5) / (2 * a)  ### condition: 'x2': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Determine the largest value of x
largest_x = max(x1, x2)  ### condition: 'largest_x': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the largest possible value of x
print(f"The largest possible value of x is: {largest_x}")