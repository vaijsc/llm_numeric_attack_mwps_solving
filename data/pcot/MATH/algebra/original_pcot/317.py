# Define the sum of the five consecutive integers
sum_of_integers = 5  ### condition: 'sum_of_integers': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Since the integers are consecutive, let the middle integer be x.
# The five consecutive integers can be represented as (x-2), (x-1), x, (x+1), (x+2).
# Thus, the sum can be expressed as:
# (x-2) + (x-1) + x + (x+1) + (x+2) = 5x = sum_of_integers
# Hence, we calculate the value of x.
x = sum_of_integers / 5  ### condition: 'x': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# The consecutive integers are (x-2), (x-1), x, (x+1), (x+2)
# Calculate the product of the five integers
product_of_integers = (x - 2) * (x - 1) * x * (x + 1) * (x + 2)  ### condition: 'product_of_integers': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Since x is calculated as a fraction, convert the product to an integer
product_of_integers = int(product_of_integers)  ### condition: 'product_of_integers': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the product of the five integers
print(f"The product of the five consecutive integers is: {product_of_integers}")