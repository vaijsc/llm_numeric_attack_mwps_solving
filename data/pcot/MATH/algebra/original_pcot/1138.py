# Define the point (0, 5)
x0 = 0  ### condition: 'x0': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
y0 = 5  ### condition: 'y0': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the point (1, 10)
x1 = 1  ### condition: 'x1': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
y1 = 10  ### condition: 'y1': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the point (2, 19)
x2 = 2  ### condition: 'x2': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
y2 = 19  ### condition: 'y2': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Create equations based on the points
# From (0, 5): c = 5
c = y0  ### condition: 'c': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# From (1, 10): a + b + c = 10; thus a + b = 10 - c
a_plus_b = y1 - c  ### condition: 'a_plus_b': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# From (2, 19): 4a + 2b + c = 19; thus 4a + 2b = 19 - c
four_a_plus_two_b = y2 - c  ### condition: 'four_a_plus_two_b': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Divide the last equation by 2 to simplify for b
two_a_plus_b = four_a_plus_two_b // 2  ### condition: 'two_a_plus_b': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Now we have two equations:
# 1. a + b = 10 - c
# 2. 2a + b = (19 - c) / 2
# Subtract the first equation from the second:
b = two_a_plus_b - a_plus_b  ### condition: 'b': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Since a + b = 10 - c
a = a_plus_b - b  ### condition: 'a': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate a + b + c
result = a + b + c  ### condition: 'result': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the sum of a, b, and c
print(f"a + b + c = {result}")