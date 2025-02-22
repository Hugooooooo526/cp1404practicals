numbers = []

for i in range(5):
    number = int(input(f"Number: "))
    numbers.append(number)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}") 
print(f"The largest number is {max(numbers)}")

# Calculate and print the average of the numbers
average = sum(numbers) / len(numbers)
print(f"The average of the numbers is {average:.2f}")


# Define the list of authorized usernames
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

# Ask the user for their username
username = input("Enter your username: ")

if username in usernames:
    print("Access Granted")
else:
    print("Access Denied")

