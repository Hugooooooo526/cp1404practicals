from guitar import Guitar
import time

def main():
    guitars = []
    print("My guitars")
    
    # Read the guitars.csv file
    with open('guitars.csv', 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            # Create a Guitar object and add it to the list
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)

    # Display all guitars
    print("\nThese are my guitars:")
    for guitar in guitars:
        print(guitar)

    # Sort by year
    guitars.sort()

    # Display guitars sorted by year
    print("\nGuitars sorted by year:")
    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    main()
    
    