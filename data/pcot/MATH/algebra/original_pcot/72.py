# Define the value of j when k = 21
j_initial = 16  ### condition: 'j_initial': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the value of k when j = 16
k_initial = 21  ### condition: 'k_initial': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the value of k when we want to find the new value of j
k_new = 14  ### condition: 'k_new': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the proportional constant
proportional_constant = j_initial * k_initial  ### condition: 'proportional_constant': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the new value of j when k = 14
j_new = proportional_constant / k_new  ### condition: 'j_new': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the new value of j
print(f"The value of j when k = 14 is: {j_new}")