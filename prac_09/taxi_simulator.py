"""
CP1404/CP5632 Practical
Taxi Simulator Program
"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Taxi simulator program that uses Taxi and SilverServiceTaxi classes."""
    total_bill = 0
    current_taxi = None
    # Create a list of taxis with different types and specifications
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    
    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    menu_choice = input(">>> ").lower()
    
    # Main program loop
    while menu_choice != 'q':
        if menu_choice == 'c':
            current_taxi = display_taxis_and_choose(taxis)
        elif menu_choice == 'd':
            total_bill = drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")
        
        print(f"Bill to date: ${total_bill:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        menu_choice = input(">>> ").lower()
    
    # Display final results
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis_and_choose(taxis):
    """Display taxis and get user's choice."""
    display_taxis(taxis)
    try:
        # Get and validate user's taxi choice
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid taxi choice")
        return None


def display_taxis(taxis):
    """Display numbered list of taxis."""
    print("Taxis available: ")
    # Display each taxi with its index
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def drive_taxi(taxi, total_bill):
    """Drive the chosen taxi, if available."""
    if taxi is None:
        print("You need to choose a taxi before you can drive")
        return total_bill
    
    try:
        # Get distance and calculate fare
        distance = float(input("Drive how far? "))
        taxi.drive(distance)
        trip_cost = taxi.get_fare()
        print(f"Your {taxi.name} trip cost you ${trip_cost:.2f}")
        return total_bill + trip_cost
    except ValueError:
        print("Invalid distance")
        return total_bill


if __name__ == '__main__':
    main()
