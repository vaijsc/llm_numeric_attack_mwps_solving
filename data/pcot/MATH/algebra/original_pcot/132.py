# Define the sum of x and y
x_plus_y = 12 ### condition: 'x_plus_y': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}

# Define the difference of x and y
x_minus_y = 8 ### condition: 'x_minus_y': {'type': 'int', '<=': 'x_plus_y', '>=': 0, 'science_constant': False, 'direct_from_question': True}

# Calculate x by solving the equations x + y = 12 and x - y = 8
x = (x_plus_y + x_minus_y) / 2 ### condition: 'x': {'type': 'int', '<=': 'x_plus_y', '>=': 'x_minus_y', 'science_constant': False, 'direct_from_question': False}

# Calculate y by solving the equations x + y = 12 and x - y = 8
y = (x_plus_y - x_minus_y) / 2 ### condition: 'y': {'type': 'int', '<=': 'x_plus_y', '>=': 0, 'science_constant': False, 'direct_from_question': False}

# Calculate 2x
two_x = 2 * x ### condition: 'two_x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}

# Calculate xy
xy = x * y ### condition: 'xy': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}

# Calculate the expression 2x - xy
result = two_x - xy ### condition: 'result': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}

# Print the final result
print(f"The value of 2x - xy is: {result}")
