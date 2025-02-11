# Define the value of x for which we want to calculate f(x)
x = -2  ### condition: 'x': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the value of f(x) using the given formula f(x) = 5x^2 + 3x + 4
f_x = 5 * x**2 + 3 * x + 4  ### condition: 'f_x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of f(-2)
print(f"The value of f(-2) is: {f_x}")