# Define the percentage as a decimal for 120%
percentage_120 = 120 / 100  ### condition: 'percentage_120': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the percentage as a decimal for 130%
percentage_130 = 130 / 100  ### condition: 'percentage_130': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the first value to compute 120% on
value_1 = 30  ### condition: 'value_1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate 120% of value_1
result_120 = percentage_120 * value_1  ### condition: 'result_120': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the second value to compute 130% on
value_2 = 20  ### condition: 'value_2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate 130% of value_2
result_130 = percentage_130 * value_2  ### condition: 'result_130': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the positive difference between result_120 and result_130
positive_difference = abs(result_120 - result_130)  ### condition: 'positive_difference': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the positive difference
print(f"The positive difference is: {positive_difference}")