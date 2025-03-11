"""
Estimate time: 15 minutes
Actual time: 10 minutes
"""

"""

Sample Output (bold is user entry):

My guitars!
Name: Fender Stratocaster
Year: 2014
Cost: $765.4
Fender Stratocaster (2014) : $765.40 added.

Name:

... snip ...

These are my guitars:
Guitar 1:  Fender Stratocaster (2014), worth $    765.40
Guitar 2:       Gibson L-5 CES (1922), worth $ 16,035.40 (vintage)
Guitar 3:        Line 6 JTV-59 (2010), worth $  1,512.90
"""
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from guitar import Guitar

def main():
    guitars = []
    print("My guitars!")
    
    # Get guitar details from user input
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        print()
        name = input("Name: ")

    # Add some test data
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))

    # Print all guitars
    # Check if the guitars list is not empty
    if guitars:
        # Print header for the guitar list
        print("\nThese are my guitars:")
        # Iterate through guitars list with enumeration starting from 1
        for i, guitar in enumerate(guitars, 1):
            # Create vintage string based on guitar age - adds "(vintage)" if guitar is 50+ years old
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            # Format and print each guitar with:
            # - Index number
            # - Right-aligned name with 20 spaces
            # - Year in parentheses  
            # - Right-aligned cost with comma separators and 2 decimal places
            # - Vintage status if applicable
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth $ {guitar.cost:>10,.2f}{vintage_string}")