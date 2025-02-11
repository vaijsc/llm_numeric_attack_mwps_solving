# Define the coefficients of the first quadratic equation
a1 = 16  ### condition: 'a1': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
b1 = 36  ### condition: 'b1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
c1 = 56  ### condition: 'c1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the coefficients of the second quadratic equation
m = None  ### condition: 'm': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
n = None  ### condition: 'n': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Since both quadratics differ only in their constant terms, set up the equation for the coefficients
# Coefficient of x^2 from (mx + n)^2 is m^2, which must equal 16
m = (a1) ** 0.5  ### condition: 'm': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Coefficient of x from (mx + n)^2 is 2mn, which must equal 36
# Therefore, we can isolate n
n = (b1 / (2 * m))  ### condition: 'n': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Now calculate the product mn
mn = m * n  ### condition: 'mn': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the calculated product mn
print(f"Value of mn: {mn}")