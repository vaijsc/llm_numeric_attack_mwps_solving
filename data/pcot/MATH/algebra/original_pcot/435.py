# Define the base number for the expression 
base_number = 8  ### condition: 'base_number': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the exponent for the base number
exponent = 4  ### condition: 'exponent': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the root for the expression 
root = 12  ### condition: 'root': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
# Calculate the equivalent expression 
numerator = base_number ** exponent  ### condition: 'numerator': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the simplified form of the root expression
simplified_form = numerator ** (1 / root)  ### condition: 'simplified_form': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Convert the simplified form to a rational number (if applicable) for final output
simplified_form_rational = round(simplified_form, 4)  ### condition: 'simplified_form_rational': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the simplified form of the expression
print(f"Simplified form of the expression √[12]{base_number}^{exponent}: {simplified_form_rational}")