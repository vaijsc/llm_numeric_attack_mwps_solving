# Define Kelly's complex number
kelly_number_real = 508  ### condition: 'kelly_number_real': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
kelly_number_imaginary = 1749  ### condition: 'kelly_number_imaginary': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Define Avril's complex number
avril_number_real = -1322  ### condition: 'avril_number_real': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
avril_number_imaginary = 1949  ### condition: 'avril_number_imaginary': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the sum of their real parts
sum_real = kelly_number_real + avril_number_real  ### condition: 'sum_real': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Calculate the sum of their imaginary parts
sum_imaginary = kelly_number_imaginary + avril_number_imaginary  ### condition: 'sum_imaginary': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': False}
# Print the sum of their complex numbers
print(f"The sum of Kelly's and Avril's numbers is: {sum_real} + {sum_imaginary}i")