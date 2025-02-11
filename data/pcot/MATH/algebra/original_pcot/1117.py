# Define the sum of the two numbers
sum_of_numbers = 25  ### condition: 'sum_of_numbers': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the difference of the two numbers
difference_of_numbers = 11  ### condition: 'difference_of_numbers': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the first number (larger number)
larger_number = (sum_of_numbers + difference_of_numbers) // 2  ### condition: 'larger_number': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the second number (smaller number)
smaller_number = sum_of_numbers - larger_number  ### condition: 'smaller_number': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the smaller of the two numbers
print(f"The smaller of the two numbers is: {smaller_number}")