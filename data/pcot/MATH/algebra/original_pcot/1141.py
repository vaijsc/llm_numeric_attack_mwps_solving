# Define the sum of the digits in both John and his father's age
sum_of_digits = 5  ### condition: 'sum_of_digits': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the possible two-digit ages for John
john_age_tens = 1  ### condition: 'john_age_tens': {'type': 'int', '<=': 9, '>=': 1, 'science_constant': False, 'direct_from_question': True}
john_age_units = sum_of_digits - john_age_tens  ### condition: 'john_age_units': {'type': 'int', '<=': 9, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate John's age
john_age = john_age_tens * 10 + john_age_units  ### condition: 'john_age': {'type': 'int', '<=': 99, '>=': 10, 'science_constant': False, 'direct_from_question': False}
# Reverse the digits to find John's father's age
father_age = john_age_units * 10 + john_age_tens  ### condition: 'father_age': {'type': 'int', '<=': 99, '>=': 10, 'science_constant': False, 'direct_from_question': False}
# Assert the positive difference between their ages is 27
assert abs(father_age - john_age) == 27, "The positive difference between their ages is not 27."
# Print John's father's age
print(f"John's father's age: {father_age}")