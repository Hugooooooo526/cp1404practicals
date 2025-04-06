"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi with higher fare costs and a flagfall."""
    # Class variable for flagfall fee
    flagfall = 4.50
    
    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi instance.
        
        Args:
            name: the name of the taxi
            fuel: the fuel level of the taxi
            fanciness: float that scales the price_per_km
        """
        super().__init__(name, fuel)
        # Multiply the price_per_km by the fanciness factor
        self.price_per_km = Taxi.price_per_km * fanciness
        self.fanciness = fanciness

    def get_fare(self):
        """Calculate the total fare including flagfall fee.
        
        Returns:
            The price for the taxi trip including flagfall
        """
        # Get the fare from the parent class method and add the flagfall
        return super().get_fare() + self.flagfall

    # Class will be implemented step by step
