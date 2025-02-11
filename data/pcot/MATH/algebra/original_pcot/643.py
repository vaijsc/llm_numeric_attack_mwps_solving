# Define Lynn's normal shoe size
lynn_normal_size = 9  ### condition: 'lynn_normal_size': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define Lynn's rock-climbing shoe size
lynn_climbing_size = 42  ### condition: 'lynn_climbing_size': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define Adina's normal shoe size
adina_normal_size = 6  ### condition: 'adina_normal_size': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the proportionality factor between normal shoe size and climbing shoe size
proportionality_factor = lynn_climbing_size / lynn_normal_size  ### condition: 'proportionality_factor': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate Adina's rock-climbing shoe size using the proportionality factor
adina_climbing_size = adina_normal_size * proportionality_factor  ### condition: 'adina_climbing_size': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print Adina's required rock-climbing shoe size
print(f"Adina should rent rock-climbing shoes size: {adina_climbing_size}")