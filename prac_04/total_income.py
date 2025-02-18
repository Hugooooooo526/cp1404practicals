"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

"""
Things to do:

Study it to see how this code answers those questions so far.

Change the line that gets the income input so that it uses an f-string instead of string concatenation (+).

Problem: We have two variables that sound very similar: incomes and months. They're both plural, so they sound like they're both lists. incomes is a list of incomes, so we might assume that months is a list of months, but it's actually a scalar value that stores the number of months - an int not a list.
Refactor the months variable to a better name.
DO NOT just change it in 3 places or use find and replace... but use refactoring in PyCharm by clicking anywhere on the variable and pressing Shift+F6 (or use the context menu). Then rename it to something more meaningful, that sounds like a number not a list.
When naming variables, we can say, "This variable stores..." and the completion of that statement is usually a good name.
In this case, "This variable stores the... number of months". :)

Run the program again with some sample data and make sure it still works.
This kind of "regression testing" is important. Make sure you don't break anything!

Now, let's refactor (move) the report printing into its own function. Select those 6 lines and turn them into a new function with a good name.
When naming functions, we can say, "This function will..." and the completion of that statement is usually a good name for the function.
In this case, "This function will... print report". :)

Test again and make sure it's all good.

Double-check the report printing function you just wrote. Is it well-designed according to SRP? Does it take in _ only_ what it needs to know? Refactor it if you can make it better.
"""

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    # Rename the variable months to num_months for better readability
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        # Use f-string to format string for getting income input
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_months + 1):
        income = incomes[month - 1]
        total += income
        # Move report printing to a separate function
        print_report(month, income, total)

def print_report(month, income, total):
    """Print income report information for each month"""
    print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

main()