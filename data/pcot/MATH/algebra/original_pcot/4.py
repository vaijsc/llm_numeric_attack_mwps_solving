import math

# Define the base of the first expression
base_1 = 2 ### condition: 'base_1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}

# Define the exponent of the first expression
exponent_1 = 8 ### condition: 'exponent_1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}

# Calculate the result of 2^8
result_1 = base_1 ** exponent_1 ### condition: 'result_1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}

# Define the base of the second expression
base_2 = 4 ### condition: 'base_2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}

# Calculate x using the logarithm
exponent_2 = math.log(result_1, base_2) ### condition: 'exponent_2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}

# Print the value of x
print(f"The value of x is: {int(exponent_2)}")
