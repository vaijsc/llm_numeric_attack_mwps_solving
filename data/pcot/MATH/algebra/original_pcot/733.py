# Define the maximum price the bookstore can charge
max_price = 40  ### condition: 'max_price': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the number of books sold based on the price
# Revenue function R(p) = p * (120 - 3p)
# We need to determine the price that maximizes this revenue
# The R(p) is a quadratic function, which opens downwards, and its maximum occurs at p = -b/(2a)
# Here, a = -3 and b = 120
a = -3  ### condition: 'a': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
b = 120  ### condition: 'b': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the price that maximizes revenue
optimal_price = -b / (2 * a)  ### condition: 'optimal_price': {'type': 'float', '<=': 'max_price', '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Assert that the optimal price does not exceed the maximum price
assert optimal_price <= max_price, "Optimal price exceeds the maximum allowed price."
# Print the optimal price to maximize revenue
print(f"The optimal price to charge for the book to maximize revenue: ${optimal_price:.2f}")