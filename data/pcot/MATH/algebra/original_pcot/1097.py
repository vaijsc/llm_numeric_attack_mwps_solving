# Define the area of the plot of land
area_of_plot = 500  ### condition: 'area_of_plot': {'type': 'int', '<=': None, '>=': 500, 'science_constant': False, 'direct_from_question': True}
# Define the relationship between width and length of the plot
length_of_plot = 20  ### condition: 'length_of_plot': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the width of the plot
width_of_plot = length_of_plot + 5  ### condition: 'width_of_plot': {'type': 'int', '<=': None, '>=': 5, 'science_constant': False, 'direct_from_question': False}
# Ensure the area condition is satisfied
assert length_of_plot * width_of_plot >= area_of_plot, "The area condition is not satisfied."
# Print the width of the plot
print(f"The width of the plot is: {width_of_plot} ft")