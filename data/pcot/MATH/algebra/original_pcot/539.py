# Define the coefficients and constants in the expression
g_squared_term = 1  ### condition: 'g_squared_term': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
b_term = 12  ### condition: 'b_term': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
c_term = 1  ### condition: 'c_term': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
constant_term = 9  ### condition: 'constant_term': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the value of p
p = b_term // (2 * g_squared_term)  ### condition: 'p': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the value of q using the formula
q = constant_term - (p ** 2) * c_term  ### condition: 'q': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the value of q
print(f"Value of q: {q}")