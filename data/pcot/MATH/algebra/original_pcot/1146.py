# Define the number of birthdays Aiden has celebrated
birthdays_count = 12  ### condition: 'birthdays_count': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
# Calculate the total number of toy cars received by summing the series of cars for each birthday
total_toy_cars = (birthdays_count * (birthdays_count + 1)) // 2  ### condition: 'total_toy_cars': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the total number of toy cars received from Jo
print(f"Total toy cars received from Jo: {total_toy_cars}")