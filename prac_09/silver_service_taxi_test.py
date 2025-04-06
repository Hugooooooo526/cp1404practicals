"""
Test SilverServiceTaxi class
"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test main functions"""
    # Create taxi
    fancy_taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)
    
    print(f"Taxi details: {fancy_taxi}")
    
    print(f"Empty fare: ${fancy_taxi.get_fare():.2f}")
    assert fancy_taxi.get_fare() == 4.5
    
    # Drive 18km
    fancy_taxi.drive(18)
    print(f"After driving 18 km: {fancy_taxi}")
    
    fare = fancy_taxi.get_fare()
    print(f"Fare: ${fare:.2f}")
    
    # Check fare
    expected_fare = (18 * (1.23 * 2)) + 4.5
    assert fare == expected_fare
    print(f"Expected fare: ${expected_fare:.2f}")
    
    hummer_taxi = SilverServiceTaxi("Hummer", 200, 4)
    print(f"\nHummer taxi details: {hummer_taxi}")
    
    # Test string format
    expected_output = "Hummer, fuel=200, odo=0, 0km on current fare, $4.92/km plus flagfall of $4.50"
    assert str(hummer_taxi) == expected_output
    print("String formatting test passed.")


if __name__ == "__main__":
    main()
