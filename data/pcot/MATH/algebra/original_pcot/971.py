# Define the inner value x
x = 4  ### condition: 'x': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate f(x) = x^2 - 4*sqrt{x} + 1
f_x = x**2 - 4 * (x**0.5) + 1  ### condition: 'f_x': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate f(f(4)) by substituting f_x into the function
f_f_x = f_x**2 - 4 * (f_x**0.5) + 1  ### condition: 'f_f_x': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the final result f(f(4))
print(f"f(f(4)) = {f_f_x}")