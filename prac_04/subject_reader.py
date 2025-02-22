"""
CP1404/CP5632 Practical
Data file -> lists program
"""

import os

FILENAME = os.path.join(os.path.dirname(__file__), "subject_data.txt")

"""
Things to do:
Copy the starter code and data file from subject_reader.py and subject_data.txt
Remember to commit these before modifying them any further.

The code reads the file data and processes it into the parts variable, but we want the load_data function to return the data as a list of lists (nested list), like:
[['CP1401', 'Ada Lovelace', 192],['CP1404', 'Alan Turing', 98]]

Currently, main just prints data. Add a new function to display subject details that produces something like the following:
 output

CP1401 is taught by Ada Lovelace and has 192 students
CP1404 is taught by Alan Turing  and has  98 students
"""

def main():
    data = load_data()
    print(data)
    display_subject_details(data)  # Call the new function to display subject details


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []  # Initialize an empty list to store the data
    try:
        input_file = open(FILENAME,'r')
        for line in input_file:
            line = line.strip()  
            parts = line.split(',')  # Separate the data into its parts
            parts[2] = int(parts[2])  # Make the student number an integer
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