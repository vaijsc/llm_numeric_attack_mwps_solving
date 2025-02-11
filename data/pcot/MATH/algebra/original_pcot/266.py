# Define the coefficient of t^2 in the height equation
a = 2  ### condition: 'a': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the coefficient of t in the height equation
b = -5  ### condition: 'b': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the constant term in the height equation
c = 29  ### condition: 'c': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the time at which the minimum height occurs using the vertex formula 
t_min = -b / (2 * a)  ### condition: 't_min': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the minimum height by substituting t_min into the height equation
minimum_height = a * t_min**2 + b * t_min + c  ### condition: 'minimum_height': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Round the minimum height to the nearest foot
minimum_height_rounded = round(minimum_height)  ### condition: 'minimum_height_rounded': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the minimum height rounded to the nearest foot
print(f"Minimum height to the nearest foot: {minimum_height_rounded}")