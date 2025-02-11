# Define the positive difference between two consecutive even perfect squares
difference = 268  ### condition: 'difference': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Let the smaller even perfect square be represented as x
# The next even perfect square, being two units larger, is (x + 2)
# The difference between them can be expressed as: (x + 2)^2 - x^2 = difference
# Expanding the equation: (x^2 + 4x + 4) - x^2 = difference
# This simplifies to 4x + 4 = difference
# Therefore, we can solve for x: 4x = difference - 4
# Calculate the smaller even perfect square
x = (difference - 4) // 4  ### condition: 'x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the larger even perfect square as (x + 2)
larger_square = (x + 2) ** 2  ### condition: 'larger_square': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the larger even perfect square
print(f"The larger of the two squares is: {larger_square}")