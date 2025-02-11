# Define the initial amount saved in the bank account
initial_amount = 500  ### condition: 'initial_amount': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the annual interest rate
annual_interest_rate = 0.03  ### condition: 'annual_interest_rate': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the number of years money is saved in the account
years = 10  ### condition: 'years': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the amount in the bank account after the interest is applied
final_amount = initial_amount * (1 + annual_interest_rate) ** years  ### condition: 'final_amount': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Round the final amount to the nearest dollar
final_amount_rounded = round(final_amount)  ### condition: 'final_amount_rounded': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the total amount in Alan's bank account after 10 years
print(f"Total amount in Alan's bank account after 10 years: ${final_amount_rounded}")