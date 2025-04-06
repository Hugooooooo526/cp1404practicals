"""
CP1404/CP5632 Practical
Guitar class for representing and managing guitars
"""


class Guitar:
    """Guitar class for storing details of a guitar."""
    
    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance.
        
        name: string, the name of the guitar
        year: integer, the year the guitar was made
        cost: float, the cost of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a guitar."""
        # Format the cost with comma for thousands and 2 decimal places
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year):
        """Return how old the guitar is in years."""
        return current_year - self.year

    def is_vintage(self, current_year):
        """Return True if the guitar is 50 or more years old."""
        return self.get_age(current_year) >= 50 