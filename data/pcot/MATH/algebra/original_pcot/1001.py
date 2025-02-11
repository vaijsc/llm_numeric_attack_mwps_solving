# Define the numerator of the fraction
numerator = -7  ### condition: 'numerator': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the denominator of the fraction
denominator = 4  ### condition: 'denominator': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the fraction result
fraction_result = numerator / denominator  ### condition: 'fraction_result': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the ceiling of the fraction result
import math
ceiling_result = math.ceil(fraction_result)  ### condition: 'ceiling_result': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the final ceiling value
print(f"The ceiling of -7/4 is: {ceiling_result}")