# Define the value of y
y = 3  ### condition: 'y': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the expression (1 + y)
expression_value = 1 + y  ### condition: 'expression_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate (1 + y) raised to the power of y
result = expression_value ** y  ### condition: 'result': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the result
print(f"The value of (1 + y)^y is: {result}")