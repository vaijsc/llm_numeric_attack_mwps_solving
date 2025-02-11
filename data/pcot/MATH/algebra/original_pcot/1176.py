# Define the base and exponent for the first term 4^3
base_1 = 4 ### condition: 'base_1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
exponent_1 = 3 ### condition: 'exponent_1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}

# Calculate 4^3
term_1 = base_1 ** exponent_1 ### condition: 'term_1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}

# Define the base and exponent for the second term 2^3
base_2 = 2 ### condition: 'base_2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
exponent_2 = 3 ### condition: 'exponent_2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}

# Calculate 2^3
term_2 = base_2 ** exponent_2 ### condition: 'term_2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}

# Sum the results of 4^3 and 2^3
sum_first_part = term_1 + term_2 ### condition: 'sum_first_part': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}

# Define the base and exponent for the third term 3^3
base_3 = 3 ### condition: 'base_3': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
exponent_3 = 3 ### condition: 'exponent_3': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}

# Calculate 3^3
term_3 = base_3 ** exponent_3 ### condition: 'term_3': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}

# Define the base and exponent for the fourth term 1^3
base_4 = 1 ### condition: 'base_4': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
exponent_4 = 3 ### condition: 'exponent_4': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}

# Calculate 1^3
term_4 = base_4 ** exponent_4 ### condition: 'term_4': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}

# Sum the results of 3^3 and 1^3
sum_second_part = term_3 + term_4 ### condition: 'sum_second_part': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}

# Calculate the final result by subtracting the second sum from the first sum
final_result = sum_first_part - sum_second_part ### condition: 'final_result': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}

# Print the final result
print(f"The value of the expression is: {final_result}")
