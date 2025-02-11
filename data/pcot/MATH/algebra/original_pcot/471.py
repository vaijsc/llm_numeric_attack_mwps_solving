# Define the number of cookies
cookies = 18  ### condition: 'cookies': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the cost relationship between cookies and brownies
cookies_to_brownies_ratio = 6 / 2  ### condition: 'cookies_to_brownies_ratio': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Define the cost relationship between brownies and cupcakes
brownies_to_cupcakes_ratio = 2.5  ### condition: 'brownies_to_cupcakes_ratio': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the number of brownies for the price of eighteen cookies
brownies_for_cookies = cookies / cookies_to_brownies_ratio  ### condition: 'brownies_for_cookies': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the number of cupcakes that can be bought using the equivalent price of brownies
cupcakes_for_brownies = brownies_for_cookies * brownies_to_cupcakes_ratio  ### condition: 'cupcakes_for_brownies': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Since the final result should be an integer, apply floor function
cupcakes = int(cupcakes_for_brownies)  ### condition: 'cupcakes': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the number of cupcakes Bob can buy
print(f"Number of cupcakes Bob can buy for the price of eighteen cookies: {cupcakes}")