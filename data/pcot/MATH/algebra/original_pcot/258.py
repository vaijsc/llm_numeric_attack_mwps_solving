# Define the sum of the two numbers
sum_of_numbers = 40  ### condition: 'sum_of_numbers': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the difference of the two numbers
difference_of_numbers = 12  ### condition: 'difference_of_numbers': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the first number using the sum and difference
first_number = (sum_of_numbers + difference_of_numbers) // 2  ### condition: 'first_number': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the second number using the sum and difference
second_number = (sum_of_numbers - difference_of_numbers) // 2  ### condition: 'second_number': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the product of the two numbers
product_of_numbers = first_number * second_number  ### condition: 'product_of_numbers': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the product of the two numbers
print(f"The product of the two numbers is: {product_of_numbers}")