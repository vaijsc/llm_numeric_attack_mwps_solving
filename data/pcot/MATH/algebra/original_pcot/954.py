# Define the number of free throws made at the fifth practice
free_throws_fifth = 48  ### condition: 'free_throws_fifth': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the number of free throws made at the fourth practice
free_throws_fourth = free_throws_fifth // 2  ### condition: 'free_throws_fourth': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the number of free throws made at the third practice
free_throws_third = free_throws_fourth // 2  ### condition: 'free_throws_third': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the number of free throws made at the second practice
free_throws_second = free_throws_third // 2  ### condition: 'free_throws_second': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the number of free throws made at the first practice
free_throws_first = free_throws_second // 2  ### condition: 'free_throws_first': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the number of free throws made at the first practice
print(f"Free throws made at the first practice: {free_throws_first}")