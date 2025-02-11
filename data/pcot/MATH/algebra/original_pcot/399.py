# Define the value of a
a = 2  ### condition: 'a': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
# Define the value of b
b = 4  ### condition: 'b': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
# Define the value of c
c = 6  ### condition: 'c': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
# Calculate the product of a, b, and c
abc = a * b * c  ### condition: 'abc': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': False}
# Calculate the sum of a, b, and c
sum_abc = a + b + c  ### condition: 'sum_abc': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': False}
# Calculate D(a, b, c)
D = abc / sum_abc  ### condition: 'D': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the result of D(2, 4, 6)
print(f"D(2, 4, 6) = {D}")