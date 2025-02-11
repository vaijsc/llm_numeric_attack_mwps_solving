# Define the fraction value
fraction_value = 2 / 5  ### condition: 'fraction_value': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the denominator for A
denominator_a = 60  ### condition: 'denominator_a': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate A using the fraction
A = fraction_value * denominator_a  ### condition: 'A': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the denominator for B
denominator_b = 60  ### condition: 'denominator_b': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Assert that the division for B will not produce a remainder
assert (denominator_b * fraction_value) % 1 == 0, "The division has a remainder, which is not allowed for this problem."
# Calculate B using the fraction
B = denominator_b / fraction_value  ### condition: 'B': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate A + B
result = A + B  ### condition: 'result': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the result of A + B
print(f"A + B = {result}")