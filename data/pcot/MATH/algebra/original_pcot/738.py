# Define the full price of one ticket
ticket_price = 20.0  ### condition: 'ticket_price': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the number of tickets Susan buys
susan_tickets = 4  ### condition: 'susan_tickets': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the discount Susan receives
susan_discount_percentage = 25.0  ### condition: 'susan_discount_percentage': {'type': 'float', '<=': 100, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the number of tickets Pam buys
pam_tickets = 5  ### condition: 'pam_tickets': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the discount Pam receives
pam_discount_percentage = 30.0  ### condition: 'pam_discount_percentage': {'type': 'float', '<=': 100, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the discount amount for Susan
susan_discount_amount = (susan_discount_percentage / 100) * (ticket_price * susan_tickets)  ### condition: 'susan_discount_amount': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the total amount Susan pays after discount
susan_total_payment = (ticket_price * susan_tickets) - susan_discount_amount  ### condition: 'susan_total_payment': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the discount amount for Pam
pam_discount_amount = (pam_discount_percentage / 100) * (ticket_price * pam_tickets)  ### condition: 'pam_discount_amount': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the total amount Pam pays after discount
pam_total_payment = (ticket_price * pam_tickets) - pam_discount_amount  ### condition: 'pam_total_payment': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the difference in payments between Pam and Susan
payment_difference = pam_total_payment - susan_total_payment  ### condition: 'payment_difference': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the difference in payments
print(f"Pam pays ${payment_difference:.2f} more than Susan.")