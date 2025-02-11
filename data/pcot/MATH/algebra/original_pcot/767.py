# Define the initial expression components
six_squared = 6 ** 2  ### condition: 'six_squared': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
three_times_eleven = 3 * 11  ### condition: 'three_times_eleven': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the expression inside the brackets
expression_inside_brackets = six_squared - three_times_eleven  ### condition: 'expression_inside_brackets': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Multiply by 8
eight_times_expression = 8 * expression_inside_brackets  ### condition: 'eight_times_expression': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Assert that 8 divides evenly into the result
assert eight_times_expression % 8 == 0, "The division has a remainder, which is not allowed for this problem."
# Calculate the division by 8
result_after_division = eight_times_expression // 8  ### condition: 'result_after_division': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the additional number to add
additional_number = 3  ### condition: 'additional_number': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the final result
final_result = result_after_division + additional_number  ### condition: 'final_result': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"The final result is: {final_result}")