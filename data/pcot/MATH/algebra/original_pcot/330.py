# Define the first number to be squared
num1 = 1002  ### condition: 'num1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the second number to be squared
num2 = 502   ### condition: 'num2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the third number to be squared
num3 = 298   ### condition: 'num3': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the fourth number to be squared
num4 = 202   ### condition: 'num4': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the difference of squares formula for the first two numbers
difference1 = num1**2 - num2**2  ### condition: 'difference1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the difference of squares formula for the last two numbers
difference2 = num3**2 - num4**2  ### condition: 'difference2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Sum the two differences calculated above
total_result = difference1 + difference2  ### condition: 'total_result': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the total result
print(f"Result of the expression 1002^2 - 502^2 + 298^2 - 202^2: {total_result}")