# Define the value of pi
pi = 3.14  ### condition: 'pi': {'type': 'float', '<=': None, '>=': 0, 'science_constant': True, 'direct_from_question': True}
# Check the range where pi falls and assign the relevant function value based on the conditions
value_of_f = 2  ### condition: 'value_of_f': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False} (since 0 <= pi < 4)
# Print the value of f(pi)
print(f"f(pi) = {value_of_f}")