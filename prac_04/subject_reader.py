"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    data = load_data()
    print(data)
    display_subject_details(data)  # Call the new function to display subject details


def load_data():
    """formatted like: subject,lecturer,number of students."""
    data = []  # Initialize an empty list to store the data
    try:
        input_file = open(FILENAME,'r')
        for line in input_file:
            line = line.strip()  # Remove \n
            parts = line.split(',')  
            parts[2] = int(parts[2])  # Make the number an integer
            data.append(parts)  # Add the processed parts to the data list
        input_file.close()
    except FileNotFoundError:
        print("File not found. Program error. Please check the code.")
    return data  # Return the list of lists


def display_subject_details(data):
    """Display subject details in a formatted string."""
    for subject, lecturer, students in data:
        print(f"{subject} is taught by {lecturer} and has {students} students")


main()