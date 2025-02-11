# Define the number to be squared
number = 989  ### condition: 'number': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the square of the number
square_of_number = number * number  ### condition: 'square_of_number': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the square of the number
print(f"The square of {number} is: {square_of_number}")