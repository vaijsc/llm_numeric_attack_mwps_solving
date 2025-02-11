# Define the equation's denominator
denominator = "x^2 - 2x + 1"  ### condition: 'denominator': {'type': 'str', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Factor the denominator to find the vertical asymptotes
factored_denominator = "(x - 1)(x - 1)"  ### condition: 'factored_denominator': {'type': 'str', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Define the values that make the denominator zero
asymptote_value = 1  ### condition: 'asymptote_value': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the values of x where there is a vertical asymptote
print(f"The value of x where there is a vertical asymptote: x = {asymptote_value}")