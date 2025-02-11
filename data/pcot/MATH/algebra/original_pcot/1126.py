# Define the constant value
constant_value = 70  ### condition: 'constant_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': True, 'direct_from_question': True}
# Define the value after subtraction
subtraction_value = 20  ### condition: 'subtraction_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the total value to equate to
total_value = 80  ### condition: 'total_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the sum of m and n
m_plus_n = total_value - constant_value + subtraction_value  ### condition: 'm_plus_n': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the coefficients for the two variables
m_coefficient = 2  ### condition: 'm_coefficient': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Assert that the equation holds given m = 2n
assert (m_coefficient + 1) * m_plus_n % (m_coefficient + 1) == 0, "The calculation for n requires valid division."
# Calculate n using the equation m = 2n -> m + n = (m_coefficient + 1)n
n_value = m_plus_n // (m_coefficient + 1)  ### condition: 'n_value': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the value of n
print(f"The value of n is: {n_value}")