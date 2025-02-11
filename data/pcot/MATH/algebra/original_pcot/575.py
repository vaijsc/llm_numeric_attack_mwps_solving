# Define the constant for the maximum value in the first square root
max_x_for_first_root = 25  ### condition: 'max_x_for_first_root': {'type': 'int', '<=': None, '>=': 0, 'science_constant': True, 'direct_from_question': True}
# Calculate the range for x in the first square root where x^2 <= 25
max_x_for_first_root_sqrt = max_x_for_first_root**0.5  ### condition: 'max_x_for_first_root_sqrt': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the point where the second square root becomes valid (x - 2 <= 0)
max_x_for_second_root = 2  ### condition: 'max_x_for_second_root': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the lower limit for the domain based on the first square root (x >= -max_x_for_first_root_sqrt)
min_x_for_first_root = -max_x_for_first_root_sqrt  ### condition: 'min_x_for_first_root': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the valid domain for x, which is from min_x_for_first_root to max_x_for_second_root
width_of_domain = max_x_for_second_root - min_x_for_first_root  ### condition: 'width_of_domain': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the width of the domain
print(f"The width of the domain for the function h(x) is: {width_of_domain}")