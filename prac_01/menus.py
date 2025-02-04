"""
pseudocode:
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

"""
example output:
Enter name: Guido
(H)ello
(G)oodbye
(Q)uit
>>> A
Invalid choice
(H)ello
(G)oodbye
(Q)uit
>>> H
Hello Guido
(H)ello
(G)oodbye
(Q)uit
>>> G
Goodbye Guido
(H)ello
(G)oodbye
(Q)uit
>>> Q
Finished.
"""

name = input("Enter name: ")
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input(">>> ").upper()
print("Finished.")