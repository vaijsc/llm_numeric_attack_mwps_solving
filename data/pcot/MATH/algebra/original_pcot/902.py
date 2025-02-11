# Define the arithmetic mean of x and y
arithmetic_mean = 7  ### condition: 'arithmetic_mean': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the geometric mean of x and y
geometric_mean = 19 ** 0.5  ### condition: 'geometric_mean': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the sum of x and y (since arithmetic mean = (x + y) / 2)
sum_xy = arithmetic_mean * 2  ### condition: 'sum_xy': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the product of x and y (since geometric mean = sqrt(x * y))
product_xy = geometric_mean ** 2  ### condition: 'product_xy': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Using the identity x^2 + y^2 = (x + y)^2 - 2xy, calculate x^2 + y^2
x_squared_plus_y_squared = sum_xy**2 - 2 * product_xy  ### condition: 'x_squared_plus_y_squared': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the result
print(f"x^2 + y^2 = {x_squared_plus_y_squared}")