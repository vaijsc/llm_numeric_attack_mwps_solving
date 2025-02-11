# Define the calories in an 8 fluid ounce bottle
calories_per_8_oz = 125  ### condition: 'calories_per_8_oz': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the volume of the bottle in fluid ounces
volume_oz = 12  ### condition: 'volume_oz': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the calories per fluid ounce
calories_per_oz = calories_per_8_oz / 8.0  ### condition: 'calories_per_oz': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the total calories in a 12 fluid ounce bottle
total_calories = calories_per_oz * volume_oz  ### condition: 'total_calories': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the total calories in the 12 fluid ounce bottle
print(f"Total calories in a 12 fluid ounce bottle: {total_calories:.2f}")