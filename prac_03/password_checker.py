"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""


"""
sample output:
Please enter a valid password
Your password must be between 5 and 15 characters, and contain:
    1 or more uppercase characters
    1 or more lowercase characters
    1 or more numbers
    and 1 or more special characters:  !@#$%^&*()_-=+`~,./'[]<>?{}|\
> this?
Invalid password!
> whyNot?CanIhaveThis?
Invalid password!
> 12345678901234567890aBcv@
Invalid password!
> thisISmy123Pass!
Invalid password!
> 1thisISit!
Your 10 character password is valid: 1thisISit!
"""

MIN_LENGTH = 5
MAX_LENGTH = 15
IS_SPECIAL_CHARACTER_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):

        print("Invalid password!")
        password = input("> ")

    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0
    for character in password:
        if character in SPECIAL_CHARACTERS:
            number_of_special += 1
        elif character.isdigit():
            number_of_digit += 1
        elif character.islower():
            number_of_lower += 1
        elif character.isupper():
            number_of_upper += 1
        else:
            pass

    if number_of_lower == 0 or number_of_upper == 0 or number_of_digit == 0:
        return False

    if number_of_special == 0:
        if IS_SPECIAL_CHARACTER_REQUIRED == True:
            return False
        else:
            pass

    return True


main()