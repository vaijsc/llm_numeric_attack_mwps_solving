# Define the total number of questions on the test
total_questions = 100  ### condition: 'total_questions': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the number of questions Frank answered
answered_questions = 80  ### condition: 'answered_questions': {'type': 'int', '<=': 'total_questions', '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the total points scored by Frank
total_score = 232  ### condition: 'total_score': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the points awarded for each correct answer
points_per_correct = 5  ### condition: 'points_per_correct': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the points deducted for each incorrect answer
points_per_incorrect = -2  ### condition: 'points_per_incorrect': {'type': 'int', '<=': None, '>=': None, 'science_constant': False, 'direct_from_question': True}
# Calculate the number of correct answers (let x be the number of correct answers)
# Let y be the number of incorrect answers
# Then, x + y = answered_questions and y = answered_questions - x
# Total score can be expressed as: total_score = x * points_per_correct + y * points_per_incorrect
# Substitute y into the score equation and solve for x
# total_score = x * points_per_correct + (answered_questions - x) * points_per_incorrect
# total_score = x * points_per_correct + answered_questions * points_per_incorrect - x * points_per_incorrect
# total_score = x * (points_per_correct - points_per_incorrect) + answered_questions * points_per_incorrect
# Rearranging gives us x = (total_score - answered_questions * points_per_incorrect) / (points_per_correct - points_per_incorrect)
# Calculate the number of correct answers
correct_answers = (total_score - answered_questions * points_per_incorrect) // (points_per_correct - points_per_incorrect)  ### condition: 'correct_answers': {'type': 'int', '<=': 'answered_questions', '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the number of correct answers
print(f"Number of questions answered correctly: {correct_answers}")