
def get_champions_data(filename):
    """Read data from file and return champions dictionary and countries set."""
    champions = {}
    countries = set()
    import os.path
    # Get the directory containing the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Create full path to the CSV file
    file_path = os.path.join(current_dir, filename)
    
    with open(file_path, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip header
        for line in in_file:
            #convert to list
            data = line.strip().split(",")
            name = data[0]
            country = data[1]
            if name in champions:
                champions[name] += 1
            else:
                champions[name] = 1
            #dic value
            countries.add(country)
    return champions, countries

def print_champions(champions):
    """Print champions and their win count."""
    print("Wimbledon Champions:")
    for name, count in champions.items():
        print(f"{name} {count}")

def print_countries(countries):
    """Print countries in alphabetical order."""
    countries_string = ", ".join(sorted(countries))
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(countries_string)

def main():
    """Main program to process Wimbledon data."""
    filename = "wimbledon.csv"
    champions, countries = get_champions_data(filename)
    print_champions(champions)
    print_countries(countries)

main()