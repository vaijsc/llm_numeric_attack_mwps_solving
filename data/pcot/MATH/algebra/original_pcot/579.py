# Define the total number of coins
total_coins = 11  ### condition: 'total_coins': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the total value of the coins in cents
total_value_cents = 75  ### condition: 'total_value_cents': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the value of a dime in cents
value_dime = 10  ### condition: 'value_dime': {'type': 'int', '<=': None, '>=': 0, 'science_constant': True, 'direct_from_question': True}
# Define the value of a nickel in cents
value_nickel = 5  ### condition: 'value_nickel': {'type': 'int', '<=': None, '>=': 0, 'science_constant': True, 'direct_from_question': True}
# Let 'd' be the number of dimes and 'n' be the number of nickels
# We have two equations:
# 1) d + n = total_coins
# 2) 10d + 5n = total_value_cents
# We can express 'd' in terms of 'n'
# d = total_coins - n  ### condition: 'd': {'type': 'int', '<=': 'total_coins', '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Substitute 'd' in the second equation:
# 10(total_coins - n) + 5n = total_value_cents
# Rearranging gives:
# 10 * total_coins - 10n + 5n = total_value_cents
# 10 * total_coins - 5n = total_value_cents
# 5n = 10 * total_coins - total_value_cents
# n = (10 * total_coins - total_value_cents) / 5
# Calculate the number of nickels
n = (10 * total_coins - total_value_cents) // value_nickel  ### condition: 'n': {'type': 'int', '<=': 'total_coins', '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the number of nickels
print(f"Number of nickels Hillary has: {n}")