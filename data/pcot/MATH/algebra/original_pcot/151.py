# Define the coefficients of the quadratic equation
a_coefficient = 2  ### condition: 'a_coefficient': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
b_coefficient = -7  ### condition: 'b_coefficient': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
c_coefficient = 2  ### condition: 'c_coefficient': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
# Calculate the discriminant of the quadratic equation
discriminant = b_coefficient**2 - 4 * a_coefficient * c_coefficient  ### condition: 'discriminant': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Assert that the discriminant is non-negative
assert discriminant >= 0, "The discriminant must be non-negative for real roots."
# Calculate the roots of the quadratic equation
root_a = (-b_coefficient + discriminant**0.5) / (2 * a_coefficient)  ### condition: 'root_a': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
root_b = (-b_coefficient - discriminant**0.5) / (2 * a_coefficient)  ### condition: 'root_b': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the expression (1/(a-1) + 1/(b-1))
expression_result = (1 / (root_a - 1)) + (1 / (root_b - 1))  ### condition: 'expression_result': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the result of the expression
print(f"The result of the expression is: {expression_result}")