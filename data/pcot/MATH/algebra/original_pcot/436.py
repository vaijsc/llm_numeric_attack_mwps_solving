# Define the coefficients of the quadratic equation
a = 1  ### condition: 'a': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
b = -2  ### condition: 'b': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
c = -3  ### condition: 'c': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the discriminant
discriminant = b**2 - 4*a*c  ### condition: 'discriminant': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate roots using the quadratic formula
p = (-b + discriminant**0.5) / (2*a)  ### condition: 'p': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
q = (-b - discriminant**0.5) / (2*a)  ### condition: 'q': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate (p + 1)(q + 1)
result = (p + 1) * (q + 1)  ### condition: 'result': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the result
print(f"The value of (p + 1)(q + 1) is: {result}")