# Define the speed of the car in miles per hour
speed_mph = 50  ### condition: 'speed_mph': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the travel time in hours as a mixed number (2 + 3/4)
mixed_number_hours = 2 + 3/4  ### condition: 'mixed_number_hours': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the total distance traveled
distance_traveled = speed_mph * mixed_number_hours  ### condition: 'distance_traveled': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Since we want to display the answer in a mixed number format, we separate the integer and fractional parts
integer_part = int(distance_traveled)  ### condition: 'integer_part': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
fractional_part = distance_traveled - integer_part  ### condition: 'fractional_part': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Convert the fractional part into a fraction of 4 (to express as a mixed number)
numerator = round(fractional_part * 4)  ### condition: 'numerator': {'type': 'int', '<=': 4, '>=': 0, 'science_constant': False, 'direct_from_question': False}
assert numerator % 1 == 0, "The numerator should be an integer."
# Print the total distance traveled as a mixed number
print(f"Distance traveled: {integer_part} {numerator}/4 miles")