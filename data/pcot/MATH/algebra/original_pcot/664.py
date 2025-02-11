# Define the coefficients of the quadratic equation
a = 1  ### condition: 'a': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
b = 24  ### condition: 'b': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
c = 128  ### condition: 'c': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the discriminant
discriminant = (b ** 2) - (4 * a * c)  ### condition: 'discriminant': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Assert that the discriminant is non-negative
assert discriminant >= 0, "The discriminant must be non-negative for real roots."
# Calculate the two roots using the quadratic formula
root1 = (-b + (discriminant ** 0.5)) / (2 * a)  ### condition: 'root1': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
root2 = (-b - (discriminant ** 0.5)) / (2 * a)  ### condition: 'root2': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Determine the largest root
largest_root = max(root1, root2)  ### condition: 'largest_root': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the largest value of x
print(f"The largest value of x is: {largest_root}")