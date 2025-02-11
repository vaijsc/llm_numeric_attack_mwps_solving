# Given problem: If $(x + y)^2 = 105$ and $x^2 + y^2 = 65$, what is the value of $xy$?
# Define the value of (x + y)^2
sum_square = 105  ### condition: 'sum_square': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the value of x^2 + y^2
sum_of_squares = 65  ### condition: 'sum_of_squares': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the value of xy using the identity x^2 + y^2 = (x + y)^2 - 2xy
# Rearranging gives us 2xy = (x + y)^2 - (x^2 + y^2)
# Thus, xy = ((x + y)^2 - (x^2 + y^2)) / 2
# Assert that the subtraction will not produce a remainder
assert (sum_square - sum_of_squares) % 2 == 0, "The division has a remainder, which is not allowed for this problem."
# Calculate xy
xy_value = (sum_square - sum_of_squares) // 2  ### condition: 'xy_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of xy
print(f"The value of xy is: {xy_value}")