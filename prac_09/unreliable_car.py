from prac_09.car import Car
import random

class UnreliableCaår(Car):
    def __init__(self,  reliability=0.0, **kwargs):
        """Initialize an UnreliableCar instance."""
        super().__init__(**kwargs)
        self.reliability = reliability
        
        
        
    def drive(self, distance):
        random_number = random.randint(0.0,100.0)
        self.distance = distance
        is_Drive = False
        if random_number > distance:
            is_Drive = True
            self.distance += distance
            
        return distance
            
    def __str__(self):
        return super().__str__()
    
    