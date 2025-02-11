# Define the product of the square roots as per the equation
product = 30  ### condition: 'product': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the coefficients for the square roots
coeff1 = 5  ### condition: 'coeff1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
coeff2 = 10 ### condition: 'coeff2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
coeff3 = 18 ### condition: 'coeff3': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the product of the coefficients
coeff_product = coeff1 * coeff2 * coeff3  ### condition: 'coeff_product': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Assert that the product calculation is correct within the square root context
assert product % coeff_product == 0, "The product has a remainder, which is not allowed for this problem."
# Calculate the value of x from the equation
x_value = (product ** 2) / coeff_product  ### condition: 'x_value': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Convert x_value to int as per the context needed
x_value = int(x_value)  ### condition: 'x_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of x
print(f"The value of x is: {x_value}")