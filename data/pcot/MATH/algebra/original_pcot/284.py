# Define the coefficients of the quadratic equation
a_coefficient = -2  ### condition: 'a_coefficient': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
b_coefficient = 4  ### condition: 'b_coefficient': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
c_coefficient = 5  ### condition: 'c_coefficient': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the vertex h value using the formula -b/(2a)
h_value = -b_coefficient / (2 * a_coefficient)  ### condition: 'h_value': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate k using the expression f(h) = a(h^2) + b(h) + c
k_value = a_coefficient * (h_value ** 2) + b_coefficient * h_value + c_coefficient  ### condition: 'k_value': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the value of k
print(f"The value of k is: {k_value}")