# Define the initial number of cells
initial_cells = 2  ### condition: 'initial_cells': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the total duration in days
total_days = 15  ### condition: 'total_days': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the duration for each splitting cycle
splitting_cycle = 3  ### condition: 'splitting_cycle': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the number of splitting cycles completed in the total duration
cycles_completed = total_days // splitting_cycle  ### condition: 'cycles_completed': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the total number of cells after all splitting cycles
total_cells = initial_cells * (2 ** cycles_completed)  ### condition: 'total_cells': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the total number of cells at the end of the 15th day
print(f"Total number of cells at the end of the 15th day: {total_cells}")