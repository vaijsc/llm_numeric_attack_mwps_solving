# Define the first polynomial
first_polynomial = "x^2 - 5*x + 7"  ### condition: 'first_polynomial': {'type': 'str', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the second polynomial represented as factored form
second_polynomial_factored = "(x - 3)*(x - 2)"  ### condition: 'second_polynomial_factored': {'type': 'str', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Expand the second polynomial
second_polynomial_expanded = "x^2 - 5*x + 6"  ### condition: 'second_polynomial_expanded': {'type': 'str', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Combine the two polynomials
result_polynomial = first_polynomial + " - (" + second_polynomial_expanded + ")"  ### condition: 'result_polynomial': {'type': 'str', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Simplify the result polynomial
simplified_polynomial = "x^2 - 5*x + 7 - x^2 + 5*x - 6"  ### condition: 'simplified_polynomial': {'type': 'str', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Further simplify the expression
final_result = "1"  ### condition: 'final_result': {'type': 'str', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the simplified polynomial
print(f"Simplified polynomial: {final_result}")