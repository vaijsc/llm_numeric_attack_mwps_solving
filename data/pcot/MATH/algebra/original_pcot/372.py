# Define the value of x
x = 15  ### condition: 'x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the value of y
y = 5  ### condition: 'y': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate (x + y)
sum_xy = x + y  ### condition: 'sum_xy': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate (x - y)
difference_xy = x - y  ### condition: 'difference_xy': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the expression (x + y)(x - y)
result = sum_xy * difference_xy  ### condition: 'result': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the result of the expression
print(f"The result of (x + y)(x - y) is: {result}")