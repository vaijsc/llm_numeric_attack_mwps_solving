# Define the x-coordinate and y-coordinate of the first point
x1 = -1  ### condition: 'x1': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
y1 = 0   ### condition: 'y1': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the x-coordinate and y-coordinate of the second point
x2 = 0   ### condition: 'x2': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
y2 = 5   ### condition: 'y2': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the x-coordinate and y-coordinate of the third point
x3 = 5   ### condition: 'x3': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
y3 = 0   ### condition: 'y3': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Set up the system of equations based on the parabola equation ax^2 + bx + c
# For point (x1, y1): a(-1)^2 + b(-1) + c = 0  =>  a - b + c = 0
# For point (x2, y2): a(0)^2 + b(0) + c = 5  =>  c = 5
# For point (x3, y3): a(5)^2 + b(5) + c = 0  =>  25a + 5b + c = 0
# From the second equation, we know c
c = 5   ### condition: 'c': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Substitute c into the first equation: a - b + 5 = 0
# Rearranging gives us a - b = -5
# Substitute c into the third equation: 25a + 5b + 5 = 0
# Rearranging gives us 25a + 5b = -5
# Thus we have two equations: a - b = -5 and 25a + 5b = -5
# Solve for b in terms of a using the first equation: b = a + 5
# Substitute b into the second equation: 25a + 5(a + 5) = -5
# Expanding gives us 25a + 5a + 25 = -5
# Combining terms gives us 30a + 25 = -5
# Rearranging gives us 30a = -30
# Solve for a
a = -1  ### condition: 'a': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Substitute a back to find b: b = a + 5
b = a + 5  ### condition: 'b': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the final value of 100a + 10b + c
result = 100 * a + 10 * b + c  ### condition: 'result': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"The value of 100a + 10b + c: {result}")