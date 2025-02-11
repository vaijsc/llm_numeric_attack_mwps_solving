# Define the number of hours in the period
total_hours = 12  ### condition: 'total_hours': {'type': 'int', '<=': 12, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the total number of chimes by summing the first n natural numbers
total_chimes = (total_hours * (total_hours + 1)) // 2  ### condition: 'total_chimes': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the total number of chimes
print(f"Total number of chimes the clock will strike in a twelve-hour period: {total_chimes}")