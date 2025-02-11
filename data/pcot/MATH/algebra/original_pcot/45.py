# Define the complex number (1 + 2i)
a = 1  ### condition: 'a': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
b = 2  ### condition: 'b': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the multiplier for the complex number
multiplier = 6  ### condition: 'multiplier': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the product of (1 + 2i) and 6
real_part = a * multiplier  ### condition: 'real_part': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
imaginary_part = b * multiplier  ### condition: 'imaginary_part': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the complex number (-3i)
c = -3  ### condition: 'c': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Combine the results to evaluate the expression (1 + 2i)6 - 3i
total_real_part = real_part  ### condition: 'total_real_part': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
total_imaginary_part = imaginary_part + c  ### condition: 'total_imaginary_part': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"Result of the expression (1 + 2i) * 6 - 3i is: {total_real_part} + {total_imaginary_part}i")