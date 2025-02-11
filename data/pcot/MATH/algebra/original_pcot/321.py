# Define the equation in terms of powers of 3
# Rewriting 9 as 3^2 gives us:
# 3^(x + 8) = (3^2)^(x + 3), which simplifies to 3^(x + 8) = 3^(2(x + 3))
# Hence, we can set the exponents equal to each other
# Define the exponent on the left-hand side
left_exponent = 'x + 8'  ### condition: 'left_exponent': {'type': 'str', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Define the exponent on the right-hand side
right_exponent = '2 * (x + 3)'  ### condition: 'right_exponent': {'type': 'str', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Set the left and right exponents equal to each other
# x + 8 = 2 * (x + 3)
# On simplifying we will get:
# x + 8 = 2x + 6
# Rearranging gives:
# 8 - 6 = 2x - x
# 2 = x
# Calculate the value of x
x = 2  ### condition: 'x': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the value of x
print(f"The value of x is: {x}")