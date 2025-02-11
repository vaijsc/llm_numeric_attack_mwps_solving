# Define the variable x
x = 0  ### condition: 'x': {'type': 'int', '<=': None, '>=': -10**6, 'science_constant': False, 'direct_from_question': False}
# Calculate the expression (x + 3)(x - 1)
expression_part1 = (x + 3) * (x - 1)  ### condition: 'expression_part1': {'type': 'int', '<=': None, '>=': -10**6, 'science_constant': False, 'direct_from_question': False}
# Calculate the expression x(x + 2)
expression_part2 = x * (x + 2)  ### condition: 'expression_part2': {'type': 'int', '<=': None, '>=': -10**6, 'science_constant': False, 'direct_from_question': False}
# Simplify the whole expression by subtracting the second part from the first
simplified_expression = expression_part1 - expression_part2  ### condition: 'simplified_expression': {'type': 'int', '<=': None, '>=': -10**6, 'science_constant': False, 'direct_from_question': False}
# Print the simplified expression
print(f"Simplified expression: {simplified_expression}")