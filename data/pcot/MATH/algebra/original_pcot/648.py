# Define the total cost of a sombrero and a pair of flip-flops
cost_sombrero_flip_flops = 32  ### condition: 'cost_sombrero_flip_flops': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the total cost of flip-flops and sunglasses
cost_flip_flops_sunglasses = 42  ### condition: 'cost_flip_flops_sunglasses': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the total cost of a sombrero and sunglasses
cost_sombrero_sunglasses = 30  ### condition: 'cost_sombrero_sunglasses': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the cost of the flip-flops using the three equations
# cost_sombrero + cost_flip_flops = 32
# cost_flip_flops + cost_sunglasses = 42
# cost_sombrero + cost_sunglasses = 30
# To find cost_flip_flops, we can solve the equations
cost_flip_flops = (cost_sombrero_flip_flops + cost_flip_flops_sunglasses - cost_sombrero_sunglasses) / 2  ### condition: 'cost_flip_flops': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the cost of the sombrero using the first equation
cost_sombrero = cost_sombrero_flip_flops - cost_flip_flops  ### condition: 'cost_sombrero': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the cost of the sombrero
print(f"The cost of the sombrero is: ${cost_sombrero}")