# Define the percentage of 50%
percentage_50 = 0.50  ### condition: 'percentage_50': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the value to calculate 50% of
value_80 = 80  ### condition: 'value_80': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate 50% of 80
half_of_80 = percentage_50 * value_80  ### condition: 'half_of_80': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the percentage of 20%
percentage_20 = 0.20  ### condition: 'percentage_20': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate 20% of the result from the previous step
twenty_percent_of_half_of_80 = percentage_20 * half_of_80  ### condition: 'twenty_percent_of_half_of_80': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"20% of 50% of 80 is: {twenty_percent_of_half_of_80}")