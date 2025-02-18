"""
Write a program that prompts the user to enter 5 numbers, then stores each number in a list named numbers.
The program should then output information about these numbers, as shown in the following output.
You can use the functions min, max, and sum, or you can use methods to add numbers to the list.

   Number: 5
   Number: 20
   Number: 1
   Number: 2
   Number: 3
   The first number is 5
   The last number is 3
   The smallest number is 1
   The largest number is 20
   The average of the numbers is 6.2
"""

# Create an empty list to store the numbers
numbers = []

# Prompt the user to enter 5 numbers
for i in range(5):
    number = int(input(f"Number: "))
    # Append the number to the list
    numbers.append(number)

# Print the first number
print(f"The first number is {numbers[0]}")

# Print the last number
print(f"The last number is {numbers[-1]}")

# Print the smallest number
print(f"The smallest number is {min(numbers)}")

# Print the largest number
print(f"The largest number is {max(numbers)}")

# Calculate and print the average of the numbers
average = sum(numbers) / len(numbers)
print(f"The average of the numbers is {average:.2f}")

"""
Copy the following username list:

   usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'] 
Ask the user for their username. If the username is in the above authorized user list, print "Access Granted", otherwise print "Access Denied".
"""

# Define the list of authorized usernames
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

# Ask the user for their username
username = input("Enter your username: ")

# Check if the username is in the authorized list
if username in usernames:
    print("Access Granted")
else:
    print("Access Denied")

