# Define the total number for the calculation
total_number = 36  ### condition: 'total_number': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the fraction to calculate (1/3)
fraction = 1/3  ### condition: 'fraction': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate one third of the total number
one_third_of_total = total_number * fraction  ### condition: 'one_third_of_total': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the percentage to calculate (50%)
percentage = 50 / 100  ### condition: 'percentage': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate 50% of one third of the total number
result = one_third_of_total * percentage  ### condition: 'result': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the result
print(f"50% of 1/3 of 36 is: {result}")