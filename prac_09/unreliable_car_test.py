"""
CP1404/CP5632 Practical
Test the UnreliableCar class
"""
from prac_09.unreliable_car import UnreliableCar
import random


def main():
    """Test the UnreliableCar class with different reliability values."""
    # Create a very reliable car (90% chance of driving)
    reliable_car = UnreliableCar("Mostly Reliable", 100, 90)
    # Create an unreliable car (30% chance of driving)
    unreliable_car = UnreliableCar("Unreliable", 100, 30)
    
    number_of_attempts = 10
    distance_to_drive = 30
    
    print(f"\nTesting {reliable_car.name} - reliability: {reliable_car.reliability}%")
    test_car_reliability(reliable_car, number_of_attempts, distance_to_drive)
    
    print(f"\nTesting {unreliable_car.name} - reliability: {unreliable_car.reliability}%")
    test_car_reliability(unreliable_car, number_of_attempts, distance_to_drive)
    
    # Now let's do a more extensive test to verify the reliability percentage
    print("\nExtensive testing to verify reliability percentage:")
    test_reliability_percentage(50, 1000)


def test_car_reliability(car, attempts, distance):
    """Test driving a car multiple times to demonstrate its reliability."""
    successful_drives = 0
    
    for i in range(1, attempts + 1):
        # Try to drive the car
        distance_driven = car.drive(distance)
        result = "successful" if distance_driven > 0 else "unsuccessful"
        print(f"Attempt {i}: Tried to drive {distance}km - {result}. "
              f"Car's fuel is now {car.fuel} and distance driven is {distance_driven}km.")
        
        if distance_driven > 0:
            successful_drives += 1
    
    print(f"Success rate: {successful_drives}/{attempts} "
          f"({successful_drives/attempts*100:.1f}%)")


def test_reliability_percentage(reliability, trials):
    """Test if the reliability percentage matches expected outcomes over many trials."""
    test_car = UnreliableCar("Test Car", 10000, reliability)  # Lots of fuel for many tests
    successful_drives = 0
    
    for _ in range(trials):
        # Try to drive the car a small distance
        if test_car.drive(1) > 0:
            successful_drives += 1
    
    success_rate = successful_drives / trials * 100
    print(f"Car with {reliability}% reliability was tested {trials} times")
    print(f"Expected success rate: {reliability}%, Actual success rate: {success_rate:.1f}%")
    print(f"Difference: {abs(reliability - success_rate):.1f}%")

if __name__ == "__main__":
    main()
