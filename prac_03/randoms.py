import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
Question:
What did you see on line 1?
# line 1: see a random integer between 5 and 20
What was the smallest number you could have seen, what was the largest?
5 20。


What did you see on line 2?
# line 2: see a random integer between 3 and 9 with a step of 2, and it cannot produce 4

What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?


What did you see on line 3?
# line 3: You could see a random float between 2.5 and 5.5

What was the smallest number you could have seen, what was the largest?


Write code, not a comment, to produce a random number between 1 and 100 inclusive.

# Writing code to produce a random number between 1 and 100 inclusive
print(random.randint(1, 100))
"""