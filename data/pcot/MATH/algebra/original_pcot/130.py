# Define the coefficients of the quadratic equation
a_coeff = 2  ### condition: 'a_coeff': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
b_coeff = -10  ### condition: 'b_coeff': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
c_coeff = 5  ### condition: 'c_coeff': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the discriminant
discriminant = b_coeff**2 - 4 * a_coeff * c_coeff  ### condition: 'discriminant': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the two solutions using the quadratic formula
solution_a = (-b_coeff + discriminant**0.5) / (2 * a_coeff)  ### condition: 'solution_a': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
solution_b = (-b_coeff - discriminant**0.5) / (2 * a_coeff)  ### condition: 'solution_b': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Construct expressions using the solutions
expr_a = 2 * solution_a - 3  ### condition: 'expr_a': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
expr_b = 4 * solution_b - 6  ### condition: 'expr_b': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the final value of the expression (2a - 3)(4b - 6)
final_value = expr_a * expr_b  ### condition: 'final_value': {'type': 'float', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the final value
print(f"The value of (2a-3)(4b-6) is: {final_value}")