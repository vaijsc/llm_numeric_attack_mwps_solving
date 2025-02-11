# Define the perimeter of the rectangle
perimeter = 100  ### condition: 'perimeter': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the relationship between length and width
length_to_width_ratio = 4  ### condition: 'length_to_width_ratio': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Let width be w and length be 4w
# The perimeter formula is P = 2(length + width)
# Therefore, 100 = 2(4w + w) => 100 = 10w => w = 10
# Calculate the width of the rectangle
width = perimeter / (2 * (length_to_width_ratio + 1))  ### condition: 'width': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the length of the rectangle
length = length_to_width_ratio * width  ### condition: 'length': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Calculate the area of the rectangle
area = length * width  ### condition: 'area': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the area of the rectangle
print(f"The area of the rectangle in square centimeters: {area}")