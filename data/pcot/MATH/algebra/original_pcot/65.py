# Define the product of m and n
product_mn = 7  ### condition: 'product_mn': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the sum of m and n
sum_mn = 8  ### condition: 'sum_mn': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate m and n using the quadratic equation coefficients
# Since m and n are the roots of the equation x^2 - (m+n)x + mn = 0
# Coefficients: a = 1, b = -sum_mn, c = product_mn
# Using the quadratic formula: x = [-b ± sqrt(b² - 4ac)] / 2a
# Calculate the discriminant
discriminant = sum_mn**2 - 4 * product_mn  ### condition: 'discriminant': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the square root of the discriminant
sqrt_discriminant = discriminant**0.5  ### condition: 'sqrt_discriminant': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate m and n using the quadratic formula (both roots)
m = (sum_mn + sqrt_discriminant) / 2  ### condition: 'm': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
n = (sum_mn - sqrt_discriminant) / 2  ### condition: 'n': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate |m - n|
absolute_difference = abs(m - n)  ### condition: 'absolute_difference': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the absolute difference
print(f"|m - n| = {absolute_difference}")