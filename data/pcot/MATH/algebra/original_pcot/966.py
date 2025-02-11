# Define the value we want to evaluate the logarithm of
value = 27  ### condition: 'value': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
# Define the base of the logarithm
base = 3  ### condition: 'base': {'type': 'int', '<=': None, '>=': 2, 'science_constant': False, 'direct_from_question': True}
# Calculate the logarithm using the change of base formula
log_value = (value ** (1 / 3))  ### condition: 'log_value': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the logarithm value
print(f"log_{base}{value}: {log_value}")