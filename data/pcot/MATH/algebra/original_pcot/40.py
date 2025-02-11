# Define the constant coefficient of the quadratic equation
constant_term = 8  ### condition: 'constant_term': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Coefficient of x^2 in the quadratic equation
coefficient_x2 = 2  ### condition: 'coefficient_x2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Discriminant condition for the quadratic to have two distinct real roots
discriminant_condition = 'm^2 - 4 * 2 * 8 > 0'  ### condition: 'discriminant_condition': {'type': 'str', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the value of the discriminant
discriminant_value = 'm**2 - 64'  ### condition: 'discriminant_value': {'type': 'str', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Solve for m: m^2 > 64
# The solution is m < -8 or m > 8
lower_bound = -8  ### condition: 'lower_bound': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
upper_bound = 8   ### condition: 'upper_bound': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the possible values of m in interval notation
print(f"Possible values of m: (-∞, {lower_bound}) ∪ ({upper_bound}, ∞)")