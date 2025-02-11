# Define the first operand A
A = 3  ### condition: 'A': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the second operand B for the inner operation
B_inner = 1  ### condition: 'B_inner': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the inner operation 3 Ψ 1
inner_result = 2 * A + 5 * B_inner  ### condition: 'inner_result': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the first operand A for the outer operation
A_outer = 9  ### condition: 'A_outer': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the outer operation 9 Ψ (3 Ψ 1)
final_result = 2 * A_outer + 5 * inner_result  ### condition: 'final_result': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the final result
print(f"The value of 9 Ψ (3 Ψ 1) is: {final_result}")