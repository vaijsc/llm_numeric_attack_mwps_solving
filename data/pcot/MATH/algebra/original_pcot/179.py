# Define the input value for x
x = -1  ### condition: 'x': {'type': 'int', '<=': None, '>=': -3, 'science_constant': False, 'direct_from_question': True}
# Calculate the value of the function h(x)
numerator = x + 3  ### condition: 'numerator': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the denominator constant
denominator = 2  ### condition: 'denominator': {'type': 'int', '<=': None, '>=': 1, 'science_constant': True, 'direct_from_question': True}
# Assert that the numerator is non-negative before calculating the square root
assert numerator % 1 == 0, "The numerator must be a whole number for the function to be valid."
# Calculate the value of h(x)
h_x = (numerator / denominator) ** 0.5  ### condition: 'h_x': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of h(-1)
print(f"The value of h(-1) is: {h_x}")