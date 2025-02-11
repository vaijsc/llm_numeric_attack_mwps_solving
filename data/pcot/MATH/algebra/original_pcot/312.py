# Define the product of a and b
product_ab = 7  ### condition: 'product_ab': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the sum of a and b
sum_ab = 5  ### condition: 'sum_ab': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate a^2 + b^2 using the identity a^2 + b^2 = (a + b)^2 - 2ab
a_squared_plus_b_squared = (sum_ab ** 2) - (2 * product_ab)  ### condition: 'a_squared_plus_b_squared': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of a^2 + b^2
print(f"The value of a^2 + b^2 is: {a_squared_plus_b_squared}")