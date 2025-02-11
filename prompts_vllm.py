PROMPT = """Below is few examples for solving task. 
### Instruction: Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?
### Response: Natalia sold 48/2 = 24 clips in May.\nNatalia sold 48 + 24 = 72 clips altogether in April and May.\nThe answer is 72.

### Instruction: Weng earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?
### Response: Weng earns 12/60 = 0.2 per minute.\nWorking 50 minutes, she earned 0.2 x 50 = 10.\nThe answer is 10.

### Instruction: Betty is saving money for a new wallet which costs $100. Betty has only half of the money she needs. Her parents decided to give her $15 for that purpose, and her grandparents twice as much as her parents. How much more money does Betty need to buy the wallet?
### Response: In the beginning, Betty has only 100/2 = 50.\nBetty's grandparents gave her 15 * 2 = 30.\nThis means, Betty needs 100 - 50 - 30 - 15 = 5 more.\nThe answer is 5.

### Instruction: Julie is reading a 120-page book. Yesterday, she was able to read 12 pages and today, she read twice as many pages as yesterday. If she wants to read half of the remaining pages tomorrow, how many pages should she read?
### Response: Maila read 12 x 2 = 24 pages today.\nSo she was able to read a total of 12 + 24 = 36 pages since yesterday.\nThere are 120 - 36 = 84 pages left to be read.\nSince she wants to read half of the remaining pages tomorrow, then she should read 84/2 = 42 pages.\nThe answer is 42.

### Instruction: James writes a 3-page letter to 2 different friends twice a week.  How many pages does he write a year?
### Response: He writes each friend 3 * 2 = 6 pages a week\nSo he writes 6 * 2 = 12 pages every week\nThat means he writes 12 * 52 = 624 pages a year.\nThe answer is 624.

### Instruction: Mark has a garden with flowers. He planted plants of three different colors in it. Ten of them are yellow, and there are 80% more of those in purple. There are only 25% as many green flowers as there are yellow and purple flowers. How many flowers does Mark have in his garden?
### Response: There are 80/100 * 10 = 8 more purple flowers than yellow flowers.\nSo in Mark's garden, there are 10 + 8 = 18 purple flowers.\nPurple and yellow flowers sum up to 10 + 18 = 28 flowers.\nThat means in Mark's garden there are 25/100 * 28 = 7 green flowers.\nSo in total Mark has 28 + 7 = 35 plants in his garden.\nThe answer is 35.

### Instruction: Albert is wondering how much pizza he can eat in one day. He buys 2 large pizzas and 2 small pizzas. A large pizza has 16 slices and a small pizza has 8 slices. If he eats it all, how many pieces does he eat that day?
### Response: He eats 32 from the largest pizzas because 2 x 16 = 32\nHe eats 16 from the small pizza because 2 x 8 = 16\nHe eats 48 pieces because 32 + 16 = 48.\nThe answer is 48.

### Instruction: Ken created a care package to send to his brother, who was away at boarding school.  Ken placed a box on a scale, and then he poured into the box enough jelly beans to bring the weight to 2 pounds.  Then, he added enough brownies to cause the weight to triple.  Next, he added another 2 pounds of jelly beans.  And finally, he added enough gummy worms to double the weight once again.  What was the final weight of the box of goodies, in pounds?
### Response: To the initial 2 pounds of jelly beans, he added enough brownies to cause the weight to triple, bringing the weight to 2 * 3 = 6 pounds.\nNext, he added another 2 pounds of jelly beans, bringing the weight to 6 + 2 = 8 pounds.\nAnd finally, he added enough gummy worms to double the weight once again, to a final weight of 8 * 2 = 16 pounds.\nThe answer is 16."""

PROMPT_CHATGPT = """Below is few examples for solving task. 
### Instruction: Mark has a garden with flowers. He planted plants of three different colors in it. Ten of them are yellow, and there are 80% more of those in purple. There are only 25% as many green flowers as there are yellow and purple flowers. How many flowers does Mark have in his garden?
### Response: There are 80/100 * 10 = 8 more purple flowers than yellow flowers.\nSo in Mark's garden, there are 10 + 8 = 18 purple flowers.\nPurple and yellow flowers sum up to 10 + 18 = 28 flowers.\nThat means in Mark's garden there are 25/100 * 28 = 7 green flowers.\nSo in total Mark has 28 + 7 = 35 plants in his garden.\nThe answer is 35.

### Instruction: Albert is wondering how much pizza he can eat in one day. He buys 2 large pizzas and 2 small pizzas. A large pizza has 16 slices and a small pizza has 8 slices. If he eats it all, how many pieces does he eat that day?
### Response: He eats 32 from the largest pizzas because 2 x 16 = 32\nHe eats 16 from the small pizza because 2 x 8 = 16\nHe eats 48 pieces because 32 + 16 = 48.\nThe answer is 48.

### Instruction: Ken created a care package to send to his brother, who was away at boarding school.  Ken placed a box on a scale, and then he poured into the box enough jelly beans to bring the weight to 2 pounds.  Then, he added enough brownies to cause the weight to triple.  Next, he added another 2 pounds of jelly beans.  And finally, he added enough gummy worms to double the weight once again.  What was the final weight of the box of goodies, in pounds?
### Response: To the initial 2 pounds of jelly beans, he added enough brownies to cause the weight to triple, bringing the weight to 2 * 3 = 6 pounds.\nNext, he added another 2 pounds of jelly beans, bringing the weight to 6 + 2 = 8 pounds.\nAnd finally, he added enough gummy worms to double the weight once again, to a final weight of 8 * 2 = 16 pounds.\nThe answer is 16."""


TEMPLATE = """
### Instruction: {question}
### Response:"""


TEMPLATE_ZERO_SHOT = """
### Instruction: {question}
Let’s think step by step.
### Response:"""

TEMPLATE_REGEN = """
### Instruction: {question}"""