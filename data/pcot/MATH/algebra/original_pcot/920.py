# Define the number of lugs to convert
lugs_to_convert = 80  ### condition: 'lugs_to_convert': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the equivalent number of lags per 9 lags
lags_per_9 = 9  ### condition: 'lags_per_9': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the number of lags per 4 lags
lags_per_4 = 4  ### condition: 'lags_per_4': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the number of ligs per 7 ligs
ligs_per_7 = 7  ### condition: 'ligs_per_7': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate how many lags are equivalent to 80 lugs using the conversion factor
# 9 lags = 20 lugs
# Therefore, 1 lug = 9/20 lags
# To find lags from lugs: lags = lugs * (9/20)
lags_from_lugs = lugs_to_convert * lags_per_9 / 20  ### condition: 'lags_from_lugs': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate how many ligs are equivalent to the computed lags using the conversion factor
# 7 ligs = 4 lags
# Therefore, 1 lag = 7/4 ligs
# To find ligs from lags: ligs = lags * (7/4)
ligs_from_lags = lags_from_lugs * ligs_per_7 / lags_per_4  ### condition: 'ligs_from_lags': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Since we need the final answer in ligs, assert the value can be converted to an integer
assert ligs_from_lags % 1 == 0, "The final number of ligs is not an integer, which is not allowed for this problem."
# Convert to int
total_ligs = int(ligs_from_lags)  ### condition: 'total_ligs': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the total number of ligs equivalent to 80 lugs
print(f"Total ligs equivalent to 80 lugs: {total_ligs}")