# Define coefficients of the quadratic equation
a = -2  ### condition: 'a': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
b = -12  ### condition: 'b': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
c = -15  ### condition: 'c': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the x-coordinate of the vertex using the formula m = -b/(2a)
m = -b / (2 * a)  ### condition: 'm': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the y-coordinate of the vertex using the quadratic equation
n = a * m**2 + b * m + c  ### condition: 'n': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate m + n
result = m + n  ### condition: 'result': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"m + n: {result}")