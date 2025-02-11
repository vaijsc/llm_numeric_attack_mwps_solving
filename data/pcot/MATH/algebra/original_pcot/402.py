# Define the initial value of p when q is 7
p_initial = 28  ### condition: 'p_initial': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the initial value of q
q_initial = 7  ### condition: 'q_initial': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the new value of q
q_new = 49  ### condition: 'q_new': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the product of p and q (constant for inverse proportion)
constant = p_initial * q_initial  ### condition: 'constant': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the new value of p when q is 49
p_new = constant / q_new  ### condition: 'p_new': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the new value of p
print(f"The value of p when q is {q_new} is: {p_new}")