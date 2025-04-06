"""
CP1404/CP5632 Practical
UnreliableCar class
"""
from prac_09.car import Car
import random

class UnreliableCar(Car):
    """An unreliable version of Car that may not drive depending on reliability."""
        
    def __init__(self,  reliability=0.0, **kwargs):
        """Initialize an UnreliableCar instance.
        
        reliability: float between 0 and 100 representing the percentage chance of driving
        """
        super().__init__(**kwargs)
        self.reliability = reliability
        
        
        
    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel and is reliable enough
        or drive until fuel runs out return the distance actually driven.
        """
        random_number = random.uniform(0, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        return 0

    def __str__(self):
        """Return a string like a Car with name, fuel and odometer values."""
        return super().__str__()
    
    