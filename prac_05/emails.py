"""
Word Occurrences
Estimate: 10 minutes
Actual:   12 minutes
"""
email_to_name = {}

def get_name_from_email(email):
    """get name from email and return as string"""
    name = email.split('@')[0].replace('.', ' ').title()
    return name

email = input("Email: ")
while email != "":
    name = get_name_from_email(email)
    confirm = input(f"Is your name {name}? (Y/n) ")
    if confirm.lower() != "y":
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")