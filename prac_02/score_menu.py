"""
This is a complete Python program following the standard structure that uses a main and other functions.
"""
MENU = """
(G)et a valid score 
(P)rint result 
(S)how stars 
(Q)uit
"""
from score import return_result
from password_stars import print_star

def main():
    print(MENU)
    user_choice = get_valid_choice()
    user_score = -1

    while user_choice != 'q':
        while is_score(user_score) != True and user_choice != 'g':
            # 没分还不选创建分的
            print("Get valid score first!!")
            print(MENU)
            user_choice = get_valid_choice()
        if user_choice == 'g':
            user_score = get_valid_score()

        elif user_choice == 'p':
            print(return_result(user_score))

        elif user_choice == 's':
            # show stars base on points
            print_star(user_score)

        print(MENU)
        user_choice = get_valid_choice()

    print("Thanks ^ ^")


def get_valid_score():
    user_score = int(input("your score:"))
    while user_score < 0 or user_score > 100:
        print("invalid score")
        user_score = int(input("your score:"))

    return user_score

def get_valid_choice():
    user_choice = input("your choice:").lower()
    while user_choice != 'g' and user_choice != 'p' and user_choice != 's' and user_choice != 'q':
        print("invalid choice")
        print(MENU)
        user_choice = input("your choice:").lower()

    return user_choice

def is_score(user_score):
    # return True or False
    # default value is -1
    return user_score != -1

main()


