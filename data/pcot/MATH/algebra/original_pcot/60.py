# Coefficient of the quadratic equation
a = 1  ### condition: 'a': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Coefficient of the linear term
b = -14  ### condition: 'b': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Coefficient of the constant term
c = 3  ### condition: 'c': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the x value that gives the minimum value of the quadratic equation using the vertex formula
x_min = -b / (2 * a)  ### condition: 'x_min': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Since we're calculating the x value and it should be noted that it is technically a float but can represent an int 
x_min_int = int(x_min)  ### condition: 'x_min_int': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the x value that gives the minimum value of the function
print(f"The value of x that gives the minimum value for x^2 - 14x + 3 is: {x_min_int}")