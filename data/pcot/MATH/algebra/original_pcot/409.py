# Define the initial current when resistance is 3 ohms
initial_current = 40  ### condition: 'initial_current': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the initial resistance
initial_resistance = 3  ### condition: 'initial_resistance': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the new resistance
new_resistance = 20  ### condition: 'new_resistance': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the voltage using Ohm's law
voltage = initial_current * initial_resistance  ### condition: 'voltage': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the new current using Ohm's law
new_current = voltage / new_resistance  ### condition: 'new_current': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the amount of current when the resistor has a resistance of 20 ohms
print(f"The amount of current when the resistance is 20 ohms: {new_current} amperes")