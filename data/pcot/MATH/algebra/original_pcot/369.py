# Define the areas of the three faces of the prism
area1 = 30  ### condition: 'area1': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
area2 = 180  ### condition: 'area2': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
area3 = 24  ### condition: 'area3': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the product of the areas
product_of_areas = area1 * area2 * area3  ### condition: 'product_of_areas': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the volume using the formula V = sqrt(area1 * area2 * area3)
# Since we derive the edge lengths, we will use integer multiplication here followed by the calculation of the volume.
volume = (product_of_areas) ** (1/2)  ### condition: 'volume': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Volume needs to be an integer, calculate the integer values of edges using the areas
# Let (x, y, z) be the edge lengths corresponding to the areas: area1 = xy, area2 = xz, area3 = yz
# Therefore, we derive the edges:
x = (area1 * area2 // area3) ** (1/2)  ### condition: 'x': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
y = (area1 * area3 // area2) ** (1/2)  ### condition: 'y': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
z = (area2 * area3 // area1) ** (1/2)  ### condition: 'z': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the volume of the prism
final_volume = x * y * z  ### condition: 'final_volume': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the volume of the prism in cubic centimeters
print(f"The volume of the right rectangular prism is: {final_volume} cubic centimeters")