# Define the value of n
n = 3  ### condition: 'n': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the value of s using the given formula
s = n**2 - 2**n + 1  ### condition: 's': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the value of t using the given formula
t = 2 * s - s**2  ### condition: 't': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of t
print(f"The value of t when n={n} is: {t}")