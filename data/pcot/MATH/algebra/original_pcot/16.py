# Define the input value for x
x = -10  ### condition: 'x': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate f(x) for the case when x < -3
f_x_case1 = 3 * x + 5  ### condition: 'f_x_case1': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Since x = -10, which is less than -3, we will use f_x_case1
f_x = f_x_case1  ### condition: 'f_x': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the result of f(-10)
print(f"f(-10) = {f_x}")