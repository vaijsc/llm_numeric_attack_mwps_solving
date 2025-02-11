# Define the number of bricks placed per hour by each bricklayer
bricks_per_hour = 30  ### condition: 'bricks_per_hour': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the total number of bricks laid by both bricklayers
total_bricks = 600  ### condition: 'total_bricks': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the ratio of hours worked by Alan and David
alan_ratio_hours = 3  ### condition: 'alan_ratio_hours': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
# Let x be the number of hours David worked
# Alan's hours worked will be 3x
# Total bricks laid is the sum of bricks laid by both 
# Calculate the total hours worked by David and Alan
# Since Alan worked three times as many hours, if David worked x hours, total hours = x + 3x = 4x
# Therefore, total bricks = bricks_per_hour * total_hours = total_bricks
# This leads to the equation: bricks_per_hour * (x + 3x) = total_bricks
# Further simplifying gives: 30 * 4x = 600 
# We can solve for x, the number of hours David worked
# Calculate David's hours worked
david_hours_worked = total_bricks / (bricks_per_hour * (alan_ratio_hours + 1))  ### condition: 'david_hours_worked': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the total number of bricks laid by David
david_bricks_laid = bricks_per_hour * david_hours_worked  ### condition: 'david_bricks_laid': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the number of bricks David laid
print(f"David laid: {david_bricks_laid} bricks")