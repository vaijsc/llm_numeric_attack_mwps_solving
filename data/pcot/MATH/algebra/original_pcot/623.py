# Define the total age of John and his dad combined
total_age = 53  ### condition: 'total_age': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the age difference between John and his dad
age_difference = 31  ### condition: 'age_difference': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate John's age using the age difference
john_age = (total_age - age_difference) // 2  ### condition: 'john_age': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate John's dad's age
dad_age = john_age + age_difference  ### condition: 'dad_age': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print John's dad's age
print(f"John's dad's age: {dad_age}")