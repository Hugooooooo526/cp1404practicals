"""
CP1404/CP5632 Practical
Test Taxi class
"""
from prac_09.taxi import Taxi


def main():
    """Test the Taxi class."""
    
    # Create a new taxi with 100 units of fuel and $1.23/km fare
    my_taxi = Taxi("Prius 1", 100, 1.23)
    
    # Drive the taxi 40km
    my_taxi.drive(40)
    
    # Print taxi details and fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")
    
    # Start new fare
    my_taxi.start_fare()
    
    # Drive the taxi 100km
    my_taxi.drive(100)
    
    # Print taxi details and fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


# Run main program
main()
