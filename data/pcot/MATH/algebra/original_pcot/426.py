# Define the first number to be squared
number1 = 32  ### condition: 'number1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the second number to be squared
number2 = 18  ### condition: 'number2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the square of the first number
square1 = number1 ** 2  ### condition: 'square1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the square of the second number
square2 = number2 ** 2  ### condition: 'square2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the difference of the squares
difference = square1 - square2  ### condition: 'difference': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the result of the computation
print(f"Result of the computation $32^2 - 18^2$: {difference}")