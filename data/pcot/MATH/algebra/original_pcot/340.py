# Define the degree of the polynomial h
degree_h = 5  ### condition: 'degree_h': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the degree of the polynomial (x^2 - 7x + 10)
degree_x2_minus_7x_plus_10 = 2  ### condition: 'degree_x2_minus_7x_plus_10': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the degree of the polynomial g
degree_g = degree_h - degree_x2_minus_7x_plus_10  ### condition: 'degree_g': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the degree of polynomial g
print(f"The degree of polynomial g is: {degree_g}")