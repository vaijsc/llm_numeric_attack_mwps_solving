# Define the fixed charge for coming out to the house
fixed_charge = 97 - 1 * (265 - 97) / 4  ### condition: 'fixed_charge': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the charge per hour
charge_per_hour = (265 - fixed_charge) / 5  ### condition: 'charge_per_hour': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the number of hours for the two-hour repair job
hours_for_two_hour_job = 2  ### condition: 'hours_for_two_hour_job': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the total charge for the two-hour repair job
total_charge_two_hour_job = fixed_charge + charge_per_hour * hours_for_two_hour_job  ### condition: 'total_charge_two_hour_job': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the total charge for the two-hour repair job
print(f"The charge for a two-hour repair job: ${total_charge_two_hour_job:.2f}")