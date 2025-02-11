import math

# Define the coefficients of the equation x^2 + 2x - 1 = 0
a = 1 ### condition: 'a': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
b = 2 ### condition: 'b': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
c = -1 ### condition: 'c': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}

# Calculate the discriminant
discriminant = b**2 - 4 * a * c ### condition: 'discriminant': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}

# Define m as -b / (2 * a)
m = -b / (2 * a) ### condition: 'm': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}

# Calculate n as the value under the square root, which must be an integer
n = int(discriminant) ### condition: 'n': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}

# Calculate the sum m + n (with m cast to an integer)
result = int(m) + n ### condition: 'result': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}

# Print the final result for m + n
print(f"The value of m + n is: {result}")
