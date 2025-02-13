"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)

"""
Questions
When will a ValueError occur?
    When the input value is not an integer.
When will a ZeroDivisionError occur?
    When you divide a number by zero.
Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, you can add a check to ensure the divisor is not zero before performing division.
"""