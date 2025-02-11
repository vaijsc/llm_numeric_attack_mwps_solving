# Define the degree of polynomial f(x)
degree_f = 4  ### condition: 'degree_f': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the degree of polynomial g(x)
degree_g = 2  ### condition: 'degree_g': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the degree of the polynomial f(x) - g(x)
degree_result = max(degree_f, degree_g)  ### condition: 'degree_result': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the degree of the polynomial f(x) - g(x)
print(f"The degree of the polynomial f(x) - g(x) is: {degree_result}")