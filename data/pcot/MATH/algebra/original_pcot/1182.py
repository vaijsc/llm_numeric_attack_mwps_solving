# Define the initial investment amount
initial_investment = 2000  ### condition: 'initial_investment': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the annual interest rate
interest_rate = 0.05  ### condition: 'interest_rate': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the number of years the money is invested
years_invested = 18  ### condition: 'years_invested': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the total amount of interest earned
total_interest = initial_investment * interest_rate * years_invested  ### condition: 'total_interest': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the total amount of money when Frederick can collect it
total_amount = initial_investment + total_interest  ### condition: 'total_amount': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the total amount Frederick will have at age 18
print(f"Total amount Frederick will have at age 18: ${total_amount:.2f}")