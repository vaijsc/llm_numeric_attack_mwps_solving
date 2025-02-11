# Define the number of students wearing red in Angie's class
students_wearing_red_class = 11  ### condition: 'students_wearing_red_class': {'type': 'int', '<=': 'students_in_class', '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the total number of students in Angie's class
students_in_class = 24  ### condition: 'students_in_class': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the ratio of students wearing red in the class
ratio_wearing_red = students_wearing_red_class / students_in_class  ### condition: 'ratio_wearing_red': {'type': 'float', '<=': 1.0, '>=': 0.0, 'science_constant': False, 'direct_from_question': False}
# Define the total number of students in the school
total_students_school = 480  ### condition: 'total_students_school': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the estimated number of students wearing red in the school using the ratio
estimated_students_wearing_red_school = ratio_wearing_red * total_students_school  ### condition: 'estimated_students_wearing_red_school': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the estimated number of students wearing red in the school
print(f"Estimated number of students wearing red in the school: {int(estimated_students_wearing_red_school)}")