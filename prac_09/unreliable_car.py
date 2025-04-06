"""
CP1404/CP5632 Practical
UnreliableCar class
"""
from prac_09.car import Car
import random

class UnreliableCaår(Car):
    """An unreliable version of Car that may not drive depending on reliability."""
        
    def __init__(self,  reliability=0.0, **kwargs):
        """Initialize an UnreliableCar instance.
        
        reliability: float between 0 and 100 representing the percentage chance of driving
        """
        super().__init__(**kwargs)
        self.reliability = reliability
        
        
        
    def drive(self, distance):
        """Drive the car if a random number is less than the car's reliability.
        
        Returns the distance driven, which may be 0 if the car is unreliable.
        """
        # Generate a random float between 0 and 100
        random_number = random.uniform(0, 100)
        # Only drive if random number is less than reliability
        if random_number < self.reliability:
            # Call the parent class's drive method and return its result
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            # Car doesn't drive, return 0 distance
            return 0

    def __str__(self):
        return super().__str__()
    
    