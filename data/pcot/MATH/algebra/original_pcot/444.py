# Define the complex number Q
Q_real = 11  ### condition: 'Q_real': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
Q_imag = -5  ### condition: 'Q_imag': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the complex number E
E_real = 11  ### condition: 'E_real': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
E_imag = 5   ### condition: 'E_imag': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define the complex number D
D_real = 0   ### condition: 'D_real': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
D_imag = 2   ### condition: 'D_imag': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate Q * E
Q_times_E_real = Q_real * E_real - Q_imag * E_imag  ### condition: 'Q_times_E_real': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
Q_times_E_imag = Q_real * E_imag + Q_imag * E_real  ### condition: 'Q_times_E_imag': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate (Q * E) * D
result_real = Q_times_E_real * D_real - Q_times_E_imag * D_imag  ### condition: 'result_real': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
result_imag = Q_times_E_real * D_imag + Q_times_E_imag * D_real  ### condition: 'result_imag': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the result of Q * E * D
print(f"Q * E * D = {result_real} + {result_imag}i")