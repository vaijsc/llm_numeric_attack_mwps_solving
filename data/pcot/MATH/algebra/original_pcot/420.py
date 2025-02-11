# Define the coefficients for the polynomial P(x)
a = 4  ### condition: 'a': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
b = -2  ### condition: 'b': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
c = 7  ### condition: 'c': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
d = -1  ### condition: 'd': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the y-intercept of P(x) by evaluating P(0)
y_intercept_P = a * (0 ** 3) + b * (0 ** 2) + c * 0 + d  ### condition: 'y_intercept_P': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the y-intercept of Q(x) which is P(0)^2
y_intercept_Q = y_intercept_P ** 2  ### condition: 'y_intercept_Q': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the y-intercept of Q(x)
print(f"The y-intercept of Q(x) is: {y_intercept_Q}")