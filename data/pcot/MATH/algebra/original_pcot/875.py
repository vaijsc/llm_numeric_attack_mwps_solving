# Define the value of h(1) given in the problem
h_at_1 = 5  ### condition: 'h_at_1': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the value of h(-1) given in the problem
h_at_neg_1 = 1  ### condition: 'h_at_neg_1': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the variable x as the point for which we want to evaluate the function h
x = 6  ### condition: 'x': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Create the system of equations to determine a and b
# h(1) = a * 1 + b
# h(-1) = a * (-1) + b
# Therefore, we can derive two equations:
# 1. a + b = h_at_1
# 2. -a + b = h_at_neg_1
# Calculate the value of b from one of the equations
b = (h_at_1 + h_at_neg_1) / 2  ### condition: 'b': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the value of a using b
a = h_at_1 - b  ### condition: 'a': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate h(6) using the values of a and b
h_at_6 = a * x + b  ### condition: 'h_at_6': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of h(6)
print(f"h(6) = {h_at_6}")