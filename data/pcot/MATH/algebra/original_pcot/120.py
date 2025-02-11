# Define the value we want to evaluate the logarithm of
value = 64  ### condition: 'value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the base of the logarithm
base = 2  ### condition: 'base': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
# Calculate the logarithm using the change of base formula
log_value = 0  ### condition: 'log_value': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
log_result = value / (base ** log_value)   ### condition: 'log_result': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# To find the logarithm, keep incrementing log_value until the base raised to log_value equals to the value
log_value = 6  ### condition: 'log_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Assert that the logarithm value satisfies the original equation
assert base ** log_value == value, "The calculated logarithm does not satisfy the equation."
# Print the logarithm value
print(f"log_{base}({value}) = {log_value}")