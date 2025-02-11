# Define the coefficients for the quadratic denominator
a_coeff = 1  ### condition: 'a_coeff': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
b_coeff = -5  ### condition: 'b_coeff': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
c_coeff = -14  ### condition: 'c_coeff': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the roots (vertical asymptotes) of the denominator using the quadratic formula
discriminant = b_coeff**2 - 4*a_coeff*c_coeff  ### condition: 'discriminant': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Assert that the discriminant is non-negative for real roots
assert discriminant >= 0, "The discriminant must be non-negative for real roots."
# Calculate the vertical asymptotes using the quadratic formula
a = (-b_coeff + discriminant**0.5) / (2*a_coeff)  ### condition: 'a': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
b = (-b_coeff - discriminant**0.5) / (2*a_coeff)  ### condition: 'b': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the horizontal asymptote, which is determined by the leading coefficients of the numerator and denominator
c = 0.0  ### condition: 'c': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the sum of the asymptotes
sum_asymptotes = a + b + c  ### condition: 'sum_asymptotes': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the sum of the asymptotes
print(f"a + b + c = {sum_asymptotes}")