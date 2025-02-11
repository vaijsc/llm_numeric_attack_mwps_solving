# Define the numerator for the division
numerator = 123123  ### condition: 'numerator': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the denominator for the division
denominator = 1001  ### condition: 'denominator': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
# Assert that the division will not produce a remainder
assert numerator % denominator == 0, "The division has a remainder, which is not allowed for this problem."
# Calculate the result of the division
result = numerator // denominator  ### condition: 'result': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the result of the division
print(f"The value of {numerator} divided by {denominator} is: {result}")