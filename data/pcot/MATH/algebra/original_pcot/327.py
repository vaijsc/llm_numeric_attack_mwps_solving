# Define the degree of polynomial p(t)
degree_p = 7  ### condition: 'degree_p': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the degree of polynomial q(t)
degree_q = 7  ### condition: 'degree_q': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the degree of the product p(t) * q(t)
degree_product = degree_p + degree_q  ### condition: 'degree_product': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the degree of the product
print(f"The degree of p(t) * q(t) is: {degree_product}")