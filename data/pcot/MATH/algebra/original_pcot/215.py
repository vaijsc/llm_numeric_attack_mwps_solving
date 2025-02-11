# Define the sum of a and b
sum_ab = 8  ### condition: 'sum_ab': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the sum of b and c
sum_bc = -3  ### condition: 'sum_bc': {'type': 'int', '<=': None, '>=': -3, 'science_constant': False, 'direct_from_question': True}
# Define the sum of a and c
sum_ac = -5  ### condition: 'sum_ac': {'type': 'int', '<=': None, '>=': -5, 'science_constant': False, 'direct_from_question': True}
# Calculate the value of a using the sums
a = (sum_ab + sum_ac - sum_bc) / 2  ### condition: 'a': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the value of b using the sums
b = (sum_ab + sum_bc - sum_ac) / 2  ### condition: 'b': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the value of c using the sums
c = (sum_ac + sum_bc - sum_ab) / 2  ### condition: 'c': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the product abc
abc = a * b * c  ### condition: 'abc': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the value of the product abc
print(f"The value of the product abc is: {abc}")