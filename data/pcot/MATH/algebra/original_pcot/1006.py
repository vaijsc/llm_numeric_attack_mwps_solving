# Define the coefficients of the quadratic expression in the denominator
a = 2  ### condition: 'a': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
b = -8  ### condition: 'b': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
c = 7  ### condition: 'c': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the discriminant of the quadratic expression
discriminant = b**2 - 4*a*c  ### condition: 'discriminant': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Assert that the discriminant is a perfect square to find two real roots
assert discriminant >= 0, "The equation does not have real roots to make it undefined."
# Calculate the two values that will make the expression undefined
root1 = (-b + (discriminant**0.5)) / (2*a)  ### condition: 'root1': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
root2 = (-b - (discriminant**0.5)) / (2*a)  ### condition: 'root2': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the sum of the two values that make the expression undefined
sum_of_roots = root1 + root2  ### condition: 'sum_of_roots': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the sum of the two values
print(f"The sum of the two values which make the expression undefined: {sum_of_roots}")