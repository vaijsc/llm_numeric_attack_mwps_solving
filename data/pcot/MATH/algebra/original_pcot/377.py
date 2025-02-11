# Define the equation to solve for n
# Starting from the equation (n + 5) / (n - 3) = 2, we need to eliminate the fraction.
n_plus_5 = 2  # This value is derived later by rearranging the equation. ### condition: 'n_plus_5': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Rearranging the equation leads to n + 5 = 2(n - 3)
# Expressing it we deduce: n + 5 = 2n - 6 which leads to n - 2n = -6 - 5
# This simplifies to -n = -11
# Therefore n can be formulated as follows,
n = 11  ### condition: 'n': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of n
print(f"The value of n is: {n}")