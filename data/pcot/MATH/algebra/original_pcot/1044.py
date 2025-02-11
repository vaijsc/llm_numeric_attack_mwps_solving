# Define the number of positive odd integers to sum
n = 5  ### condition: 'n': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
# Calculate the sum of the first n positive odd integers
sum_of_odds = n**2  ### condition: 'sum_of_odds': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the sum of the first five positive odd integers
print(f"The sum of the first {n} positive odd integers is: {sum_of_odds}")