# Define the first term in the equation
first_term = 26**2 - 24**2 - 10  ### condition: 'first_term': {'type': 'int', '<=': None, '>=': -10, 'science_constant': False, 'direct_from_question': False}
# Define the second term in the equation
second_term = 10**2  ### condition: 'second_term': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the first term squared
first_term_squared = first_term**2  ### condition: 'first_term_squared': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the final result by subtracting the second term from the first term squared
result = first_term_squared - second_term  ### condition: 'result': {'type': 'int', '<=': None, '>=': -100, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"The value of the expression is: {result}")