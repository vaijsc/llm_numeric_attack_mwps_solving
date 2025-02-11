# Define the values of x and y
x = 3  ### condition: 'x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
y = 9  ### condition: 'y': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate y squared
y_squared = y ** 2  ### condition: 'y_squared': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the product of 3, x, and y
three_xy = 3 * x * y  ### condition: 'three_xy': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the final expression y^2 - 3xy + 8
result = y_squared - three_xy + 8  ### condition: 'result': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"The result of the expression is: {result}")