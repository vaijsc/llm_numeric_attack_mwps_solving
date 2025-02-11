# Define the base of the exponent
base = 3  ### condition: 'base': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate 3^4
power_4 = base ** 4  ### condition: 'power_4': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate 3^3
power_3 = base ** 3  ### condition: 'power_3': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate 3^2
power_2 = base ** 2  ### condition: 'power_2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the numerator: 3^4 - 3^3
numerator = power_4 - power_3  ### condition: 'numerator': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the denominator: 3^3 - 3^2
denominator = power_3 - power_2  ### condition: 'denominator': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Assert that the denominator is not zero
assert denominator != 0, "The denominator cannot be zero."
# Calculate the final result
result = numerator / denominator  ### condition: 'result': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"The result of the computation is: {result}")