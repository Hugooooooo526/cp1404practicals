"""
password_star files for prac_02 lesson
"""

# import
# MINIMUM_LENGTH = 3

def main():
    minimum_length = 6
    password = get_password(minimum_length)
    print_star_base_password(password)

def print_star_base_password(password):
    print(len(password) * "*")

def get_password(minimum_length):
    password = input("Password:")

    while len(password) < minimum_length:
        print("It is too short")
        password = str(input("Password:"))
    return password

main()


# def main():
#     user_password = int(input(""))
#     getvalidPassword(user_password)


# def getvalidPassword(user_password):


#     return user_password
