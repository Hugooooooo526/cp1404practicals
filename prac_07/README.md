# Practical 07

## Files in this Folder

- `project.py` - Contains the Project class definition with attributes and methods for project management
- `project_management.py` - Main program for the project management system with menu and functions
- `projects.txt` - Data file containing tab-delimited project information
- `programming_language.py` - Implementation of the ProgrammingLanguage class with pointer arithmetic feature
- `language_file_reader.py` - Program to read and display programming language data from CSV file
- `languages.csv` - Data file containing programming language information
- `guitar.py` - Class definition for Guitar objects with comparison capabilities
- `myguitars.py` - Program to read guitar data from CSV and demonstrate sorting
- `guitars.csv` - Data file containing guitar information

## Modifications and Implementations

### Project Management System
- Created Project class with necessary attributes and methods
- Implemented file loading and saving functionality
- Added display capabilities with sorting by priority
- Developed date filtering functionality
- Created input validation for all user inputs
- Implemented project updating features

### Programming Languages
- Added pointer arithmetic attribute to ProgrammingLanguage class
- Updated the __str__ and __repr__ methods to display the new attribute
- Modified the language_file_reader.py to handle the new attribute
- Updated the languages.csv file to include pointer arithmetic data

### Guitar Collection
- Added __lt__ method to Guitar class to enable sorting by year
- Implemented sorting functionality in myguitars.py
- Created display functionality to show guitars sorted by age

All implementations include proper error handling, input validation, and follow good programming practices.
