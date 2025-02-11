# Define Planck's constant
plancks_constant = 6.62607015e-34  ### condition: 'plancks_constant': {'type': 'float', '<=': None, '>=': 0, 'science_constant': True, 'direct_from_question': True}
# Define the original error in momentum
original_error_momentum = 1.0  ### condition: 'original_error_momentum': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the original minimum error in position using Heisenberg's Uncertainty Principle
original_error_position = plancks_constant / (4 * 3.14 * original_error_momentum)  ### condition: 'original_error_position': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Halve the error in momentum
halved_error_momentum = original_error_momentum / 2  ### condition: 'halved_error_momentum': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the new minimum error in position with the halved momentum error
new_error_position = plancks_constant / (4 * 3.14 * halved_error_momentum)  ### condition: 'new_error_position': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the increase in error position
increase_in_error_position = new_error_position - original_error_position  ### condition: 'increase_in_error_position': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the percentage increase
percentage_increase = (increase_in_error_position / original_error_position) * 100  ### condition: 'percentage_increase': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the percentage increase in the minimum error in position
print(f"The minimum error in the measurement of its position increases by {percentage_increase}%")