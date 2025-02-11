# Define the value of x for the evaluation
x_value = -3 ### condition: 'x_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}

# Define the numerator of f(x) = (x^2 + 2x + 3)
numerator_f = x_value**2 + 2 * x_value + 3 ### condition: 'numerator_f': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}

# Define the denominator of f(x) = x
denominator_f = x_value ### condition: 'denominator_f': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}

# Calculate f(x) and ensure integer type for the condition
f_x = numerator_f / denominator_f ### condition: 'f_x': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}

# Define g(f(x)) = (f(x))^3 + 2
g_f_x = f_x**3 + 2 ### condition: 'g_f_x': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}

# Print the final evaluated result
print(f"The value of g(f(x)) when x = -3 is: {int(g_f_x)}")
