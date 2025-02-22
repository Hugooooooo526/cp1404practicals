"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    # Rename the variable months to num_months for better readability
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
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