# Define the initial integer n
n = 2  ### condition: 'n': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate f(n) for the first application
if n % 2 == 0: 
    n = n**2 - 3*n + 1  ### condition: 'n after f1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
else: 
    n = n**2 + 1  ### condition: 'n after f1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate f(n) for the second application
if n % 2 == 0: 
    n = n**2 - 3*n + 1  ### condition: 'n after f2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
else: 
    n = n**2 + 1  ### condition: 'n after f2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate f(n) for the third application
if n % 2 == 0: 
    n = n**2 - 3*n + 1  ### condition: 'n after f3': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
else: 
    n = n**2 + 1  ### condition: 'n after f3': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate f(n) for the fourth application
if n % 2 == 0: 
    n = n**2 - 3*n + 1  ### condition: 'n after f4': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
else: 
    n = n**2 + 1  ### condition: 'n after f4': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate f(n) for the fifth application
if n % 2 == 0: 
    n = n**2 - 3*n + 1  ### condition: 'n after f5': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
else: 
    n = n**2 + 1  ### condition: 'n after f5': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate f(n) for the sixth application
if n % 2 == 0: 
    n = n**2 - 3*n + 1  ### condition: 'n after f6': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
else: 
    n = n**2 + 1  ### condition: 'n after f6': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the final result after six applications of f
print(f"f(f(f(f(f(f(2)))))) = {n}")