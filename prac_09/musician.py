"""
CP1404/CP5632 Practical
Musician class for representing and managing a musician with instruments
"""


class Musician:
    """Musician class for storing details of a musician and their instruments."""

    def __init__(self, name=""):
        """Initialize a Musician with a name and empty instruments list."""
        self.name = name
        self.instruments = []

    def __str__(self):
        """Return a string representation of a musician."""
        if not self.instruments:
            return f"{self.name} ([])"
        
        # Format instruments list for string representation
        instruments_string = ", ".join(str(instrument) for instrument in self.instruments)
        return f"{self.name} ([{instruments_string}])"

    def add(self, instrument):
        """Add an instrument to the musician's collection."""
        self.instruments.append(instrument)

    def play(self):
        """Return a string showing the musician playing their first instrument."""
        if not self.instruments:
            return f"{self.name} needs an instrument!"
        # Play the first instrument in the collection
        return f"{self.name} is playing: {self.instruments[0]}" 