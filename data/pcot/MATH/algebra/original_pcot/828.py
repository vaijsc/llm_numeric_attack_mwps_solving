# Define the coefficients of the polynomial
a = 1  ### condition: 'a': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
b = 7  ### condition: 'b': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
c = -2  ### condition: 'c': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the sum of the roots using the formula -b/a
sum_of_roots = -b / a  ### condition: 'sum_of_roots': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the product of the roots using the formula c/a
product_of_roots = c / a  ### condition: 'product_of_roots': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate alpha^2 + beta^2 using the relationship alpha^2 + beta^2 = (alpha + beta)^2 - 2 * (alpha * beta)
alpha_squared_plus_beta_squared = sum_of_roots**2 - 2 * product_of_roots  ### condition: 'alpha_squared_plus_beta_squared': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the result of alpha^2 + beta^2
print(f"Value of alpha^2 + beta^2: {alpha_squared_plus_beta_squared}")