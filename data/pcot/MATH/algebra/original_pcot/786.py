# Define the total degrees the Earth rotates in one day
degrees_per_day = 360  ### condition: 'degrees_per_day': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the number of hours in one day
hours_per_day = 24  ### condition: 'hours_per_day': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Assert that the number of degrees is divisible by the number of hours
assert degrees_per_day % hours_per_day == 0, "The division has a remainder, which is not allowed for this problem."
# Calculate the degrees rotated in one hour
degrees_per_hour = degrees_per_day // hours_per_day  ### condition: 'degrees_per_hour': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the degrees rotated in one hour
print(f"The Earth rotates {degrees_per_hour} degrees in one hour.")