# Define the values of h(x) based on the given problem
h_2 = 10  ### condition: 'h_2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
h_10 = 1   ### condition: 'h_10': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
h_1 = 2    ### condition: 'h_1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Since h(x) is the inverse of f(x), we find f(h(2)), which means f(10)
f_of_h_2 = h_2  ### condition: 'f_of_h_2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Since f is the inverse of h, we find h(f(10)), which corresponds to h(f_of_h_2)
f_of_h_2_value = h_1  ### condition: 'f_of_h_2_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate f(f(10)) which translates to h(f_of_h_2_value)
f_f_10 = h_10  ### condition: 'f_f_10': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of f(f(10))
print(f"f(f(10)) = {f_f_10}")