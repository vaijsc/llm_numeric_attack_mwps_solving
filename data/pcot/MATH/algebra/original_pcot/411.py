# Define the degree of the polynomial on the right side of the equation
degree_polynomial = 4  ### condition: 'degree_polynomial': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# The term (x-1) has a degree of 1
degree_term = 1  ### condition: 'degree_term': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the degree of f by subtracting the degree of the term (x-1) from the degree of the polynomial
degree_f = degree_polynomial - degree_term  ### condition: 'degree_f': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the degree of f
print(f"The degree of f is: {degree_f}")