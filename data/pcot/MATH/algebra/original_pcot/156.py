# Define the coefficient of x^2 in the quadratic equation
a = 9  ### condition: 'a': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the constant term in the quadratic equation
c = 36  ### condition: 'c': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# The condition for the quadratic equation to have exactly one solution is the discriminant must be zero
# Discriminant = b^2 - 4ac must equal 0 for one solution
# Here b corresponds to n
# Thus we set up the equation n^2 - 4 * a * c = 0
# We'll calculate 4 * a * c
discriminant_part = 4 * a * c  ### condition: 'discriminant_part': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the positive solution for n using the discriminant condition
n_positive = (discriminant_part)**0.5  ### condition: 'n_positive': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the positive value of n
print(f"The positive value of n is: {n_positive}")