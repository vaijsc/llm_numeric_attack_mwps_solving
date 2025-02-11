# Define the speed at which Alice ran
speed_m_per_s = 9.0  ### condition: 'speed_m_per_s': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the time for which Alice ran
time_seconds = 12  ### condition: 'time_seconds': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the distance ran by Alice using the formula distance = speed * time
distance_meters = speed_m_per_s * time_seconds  ### condition: 'distance_meters': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the distance Alice ran
print(f"Distance ran by Alice: {distance_meters} meters")