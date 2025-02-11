# Define the coefficients of the quadratic equation
a = 1  ### condition: 'a': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
b = -1  ### condition: 'b': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
c = -6  ### condition: 'c': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the product of the roots using the formula c/a
product_of_solutions = c / a  ### condition: 'product_of_solutions': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the product of the two solutions
print(f"The product of the two solutions is: {product_of_solutions}")