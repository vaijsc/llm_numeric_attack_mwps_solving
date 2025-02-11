# Define the total amount to calculate percentage from
total_amount = 10  ### condition: 'total_amount': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the first percentage to apply
first_percentage = 200 / 100  ### condition: 'first_percentage': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate 200% of the total amount
first_calculation = first_percentage * total_amount  ### condition: 'first_calculation': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the second percentage to apply
second_percentage = 50 / 100  ### condition: 'second_percentage': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate 50% of the first calculation
final_result = second_percentage * first_calculation  ### condition: 'final_result': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"$50% of $200% of $10 is: ${final_result}")