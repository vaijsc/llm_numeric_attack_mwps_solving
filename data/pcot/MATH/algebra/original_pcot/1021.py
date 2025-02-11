# Define the coefficients in the equations
coefficient_x = 3  ### condition: 'coefficient_x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
coefficient_y = 8  ### condition: 'coefficient_y': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
coefficient_z = 5  ### condition: 'coefficient_z': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the relationship from the first equation
# 3x = 8y can be rearranged to find the ratio of x to y
x_to_y_ratio = coefficient_y / coefficient_x  ### condition: 'x_to_y_ratio': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the relationship from the second equation
# 5y = 15z simplifies to y = 3z, which gives us the ratio of y to z
y_to_z_ratio = coefficient_z / (coefficient_z * 3)  ### condition: 'y_to_z_ratio': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the ratio of x to z using the ratios obtained
x_to_z_ratio = x_to_y_ratio * (1 / y_to_z_ratio)  ### condition: 'x_to_z_ratio': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Simplify the x to z ratio to get the value
x_to_z_value = x_to_z_ratio  ### condition: 'x_to_z_value': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of x/z in simplest form
print(f"The value of x/z is: {x_to_z_value}")