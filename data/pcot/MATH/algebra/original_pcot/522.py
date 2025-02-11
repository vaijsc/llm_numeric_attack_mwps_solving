# Define the point at which the piecewise function changes
x_switch = -4  ### condition: 'x_switch': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the value of f(-4)
f_minus_4 = -60 / 13  ### condition: 'f_minus_4': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the value of f(4)
f_4 = 3120  ### condition: 'f_4': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate a and b using the first part of the piecewise function
# Since f(-4) = (a/b)(-4), we rearrange to find a / b
a_over_b = f_minus_4 / x_switch  ### condition: 'a_over_b': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate ab using the second part of the piecewise function
# Since f(4) = ab(4^2), we rearrange to find ab
ab = f_4 / (4**2)  ### condition: 'ab': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Express 'a' in terms of 'b' using a / b = a_over_b
# Let a = a_over_b * b
# Substitute into ab = a * b to find b
# ab = (a_over_b * b) * b = a_over_b * b^2
# b^2 = ab / a_over_b
# Thus: b = sqrt(ab / a_over_b)
b = (ab / a_over_b) ** 0.5  ### condition: 'b': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate 'a' using b
a = a_over_b * b  ### condition: 'a': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the sum of a and b
sum_a_b = a + b  ### condition: 'sum_a_b': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the result of a + b
print(f"a + b = {sum_a_b}")