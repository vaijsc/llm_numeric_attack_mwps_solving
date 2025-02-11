# Define the constant values in the equation
first_value = 441  ### condition: 'first_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the multiplier for the second term
second_term_multiplier = 2  ### condition: 'second_term_multiplier': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the first value for the second term calculation
second_term_value_1 = 21  ### condition: 'second_term_value_1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the second value for the second term calculation
second_term_value_2 = 19  ### condition: 'second_term_value_2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the constant value to be added in the equation
third_value = 361  ### condition: 'third_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the second term
second_term = second_term_multiplier * second_term_value_1 * second_term_value_2  ### condition: 'second_term': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the final value of x
x = first_value + second_term + third_value  ### condition: 'x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of x
print(f"The value of x is: {x}")