# Define the number of oranges Kim can initially buy
oranges_initial = 40  ### condition: 'oranges_initial': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the initial price per orange in cents
initial_price_per_orange = 3  ### condition: 'initial_price_per_orange': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the total money Kim has in cents
total_money = oranges_initial * initial_price_per_orange  ### condition: 'total_money': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the new price per orange in cents
new_price_per_orange = 4  ### condition: 'new_price_per_orange': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Assert that the total money can be divided by the new price without remainder
assert total_money % new_price_per_orange == 0, "The division has a remainder, which is not allowed for this problem."
# Calculate the number of oranges Kim can buy at the new price
oranges_after_price_rise = total_money // new_price_per_orange  ### condition: 'oranges_after_price_rise': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the number of oranges Kim can buy after the price rise
print(f"Oranges Kim can buy after the price rise: {oranges_after_price_rise}")