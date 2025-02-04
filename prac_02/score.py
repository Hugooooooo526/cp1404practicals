"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# if elif else

def main():
    score = float(input("Enter score: "))
    result = return_result(score)
    print(result)

def return_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"

main()
