# Define the total number of games played in the tournament
total_games = 55  ### condition: 'total_games': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the formula component for the number of teams
formula_component = 2 * total_games  ### condition: 'formula_component': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Internal calculation to derive n^2 - n
# Rearranging the equation n*(n-1)/2 = total_games gives us n^2 - n - formula_component = 0
# We need to find n; we will have two possible solutions from the quadratic formula
# For the purpose of this problem, we are interested in the positive solution only
# Calculate the discriminant (D)
D = 1 + 4 * formula_component  ### condition: 'D': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the number of teams (n) using the positive solution of the quadratic formula
n = (1 + D ** 0.5) / 2  ### condition: 'n': {'type': 'float', '<=': None, '>=': 2, 'science_constant': False, 'direct_from_question': False}
# Since n must be an integer, we will take the integer value of n
n_teams = int(n)  ### condition: 'n_teams': {'type': 'int', '<=': None, '>=': 2, 'science_constant': False, 'direct_from_question': False}
# Print the total number of teams in the tournament
print(f"Number of teams in the round-robin tournament: {n_teams}")