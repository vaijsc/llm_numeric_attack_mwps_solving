# Define the sum of x and y
sum_xy = 13  ### condition: 'sum_xy': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the product of x and y
product_xy = 24  ### condition: 'product_xy': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the discriminant
discriminant = sum_xy**2 - 4 * product_xy  ### condition: 'discriminant': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the values of x and y using the quadratic formula
x = (sum_xy + (discriminant**0.5)) / 2  ### condition: 'x': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
y = (sum_xy - (discriminant**0.5)) / 2  ### condition: 'y': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the distance from the point (x, y) to the origin
distance_to_origin = (x**2 + y**2)**0.5  ### condition: 'distance_to_origin': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the distance from the point (x, y) to the origin
print(f"Distance from the point (x, y) to the origin: {distance_to_origin}")