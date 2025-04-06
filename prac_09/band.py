"""
CP1404/CP5632 Practical
Band class for representing and managing a band of musicians
"""


class Band:
    """Band class for storing details of a music band."""

    def __init__(self, name=""):
        """Initialize a Band with a name and empty musicians list."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a band."""
        if not self.musicians:
            return f"{self.name} ()"
        
        # Format musicians list for string representation
        musicians_string = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_string})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their first instrument."""
        if not self.musicians:
            return f"{self.name} has no musicians!"
        
        # Build a string of each musician playing (or needing an instrument)
        result = ""
        for musician in self.musicians:
            # Assuming Musician class has instruments attribute that is a list
            # and a play method that returns the musician playing their first instrument
            result += musician.play() + "\n"
        return result.strip() 