# Define the degree of the first polynomial
degree_poly1 = 8  ### condition: 'degree_poly1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the degree of the second polynomial
degree_poly2 = 5  ### condition: 'degree_poly2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the degree of the third polynomial
degree_poly3 = 2  ### condition: 'degree_poly3': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the total degree of the resulting polynomial
total_degree = degree_poly1 + degree_poly2 + degree_poly3  ### condition: 'total_degree': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the degree of the polynomial
print(f"The degree of the polynomial is: {total_degree}")