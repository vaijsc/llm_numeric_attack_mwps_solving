# Define the numerator of the fraction
numerator = 16  ### condition: 'numerator': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the denominator of the fraction
denominator = 625  ### condition: 'denominator': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the fourth root of the numerator
fourth_root_numerator = numerator ** (1/4)  ### condition: 'fourth_root_numerator': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the fourth root of the denominator
fourth_root_denominator = denominator ** (1/4)  ### condition: 'fourth_root_denominator': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Convert the roots to integers as the final fraction
fraction_numerator = int(fourth_root_numerator)  ### condition: 'fraction_numerator': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
fraction_denominator = int(fourth_root_denominator)  ### condition: 'fraction_denominator': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the common fraction
print(f"The common fraction is: {fraction_numerator}/{fraction_denominator}")