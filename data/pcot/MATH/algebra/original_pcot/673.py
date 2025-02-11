# Define the calories in a snack-size tin of peaches
calories_per_tin = 40  ### condition: 'calories_per_tin': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the percentage of daily caloric requirement that the tin represents
percentage_of_daily_requirement = 2.0  ### condition: 'percentage_of_daily_requirement': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the daily caloric requirement
daily_caloric_requirement = calories_per_tin / (percentage_of_daily_requirement / 100)  ### condition: 'daily_caloric_requirement': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the daily caloric requirement
print(f"Daily caloric requirement: {daily_caloric_requirement}")