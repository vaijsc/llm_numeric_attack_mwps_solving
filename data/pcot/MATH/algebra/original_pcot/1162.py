# Define the numerator of the expression
numerator = (1/2) * 1024  ### condition: 'numerator': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the base and exponent for the denominator
base = 2  ### condition: 'base': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
exponent = 12  ### condition: 'exponent': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the denominator using the given constant for multiplication
denominator = 0.125 * (base ** exponent)  ### condition: 'denominator': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Assert that the denominator is not zero to avoid division by zero
assert denominator != 0, "Denominator cannot be zero."
# Calculate the simplified value of the expression
simplified_value = numerator / denominator  ### condition: 'simplified_value': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the simplified value of the expression
print(f"Simplified value: {simplified_value}")