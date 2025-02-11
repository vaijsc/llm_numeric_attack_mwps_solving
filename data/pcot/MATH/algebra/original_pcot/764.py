# Define the value for which we need to find g
value_for_g = -3  ### condition: 'value_for_g': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the coefficients for the quadratic equation
a = 4  ### condition: 'a': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
b = -3  ### condition: 'b': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
c = 2  ### condition: 'c': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the value of x that corresponds to g(-3)
# We need to solve the equation 2x + 5 = -3 to find x
# Rearranging gives us 2x = -3 - 5 -> 2x = -8
# thus, x = -8/2 
assert (-8) % 2 == 0, "The division has a remainder, which is not allowed for this problem."
x_for_g = -8 // 2  ### condition: 'x_for_g': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate g(x_for_g)
g_value = a * (x_for_g ** 2) + b * x_for_g + c  ### condition: 'g_value': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the result of g(-3)
print(f"g(-3) = {g_value}")