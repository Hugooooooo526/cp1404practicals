"""
password_star files for prac_02 lesson
"""

# import
# MINIMUM_LENGTH = 3

def main():
    minimum_length = 6
    password = get_password(minimum_length)
    print_star(len(password))

def print_star(number):
    print(number * "*")

def get_password(minimum_length):
    password = input("Password:")

    while len(password) < minimum_length:
        print("It is too short")
        password = str(input("Password:"))
    return password

# main()
