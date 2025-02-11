# Define the coefficient of x^2 in the expression
a = -2  ### condition: 'a': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the coefficient of x in the expression
b = -20  ### condition: 'b': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the constant term in the expression
c = -53  ### condition: 'c': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the value of d using the formula d = b/(2a)
d = b / (2 * a)  ### condition: 'd': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate e using the formula e = c - (b^2/(4a))
e = c - (b ** 2) / (4 * a)  ### condition: 'e': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the sum of a, d, and e
sum_a_d_e = a + d + e  ### condition: 'sum_a_d_e': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the sum of a, d, and e
print(f"The sum a + d + e is: {sum_a_d_e}")