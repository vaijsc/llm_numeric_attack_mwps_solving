# Define the coefficient of x^2
a = 2  ### condition: 'a': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the coefficient of x
b = -8  ### condition: 'b': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the constant term
c = 15  ### condition: 'c': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the discriminant using the formula D = b^2 - 4ac
discriminant = b**2 - 4 * a * c  ### condition: 'discriminant': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the discriminant
print(f"The discriminant of the equation is: {discriminant}")