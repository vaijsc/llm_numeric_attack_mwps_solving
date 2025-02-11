# Define the first complex number
a = 5  ### condition: 'a': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
b = -3  ### condition: 'b': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the second complex number
c = -4  ### condition: 'c': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
d = 3  ### condition: 'd': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the real part of the product
real_part = a * c - b * d  ### condition: 'real_part': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the imaginary part of the product
imaginary_part = a * d + b * c  ### condition: 'imaginary_part': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the simplified product
print(f"Simplified form of (5-3i)(-4+3i): {real_part} + {imaginary_part}i")