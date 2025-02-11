# Define the maximum exponent for the term in the series
max_exponent = 10  ### condition: 'max_exponent': {'type': 'int', '<=': None, '>=': 1, 'science_constant': False, 'direct_from_question': True}
# Calculate the sum of the series using the formula for a geometric series
# The sum from k=1 to max_exponent of (1 / 2^k) can be calculated as 1 - (1 / 2^max_exponent) 
# divided by (1 - 1/2), which simplifies to 1 - (1 / 2^max_exponent)
sum_series = 1 - (1 / (2 ** max_exponent))  ### condition: 'sum_series': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Since the problem requires a common fraction, we express the sum as a fraction
# The common fraction representation is (2^max_exponent - 1) / (2^max_exponent)
numerator = (2 ** max_exponent) - 1  ### condition: 'numerator': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
denominator = (2 ** max_exponent)  ### condition: 'denominator': {'type': 'int', '<=': None, '>=': 1, 'science_constant': True, 'direct_from_question': False}
# Print the common fraction representation
print(f"The sum expressed as a common fraction is: {numerator}/{denominator}")