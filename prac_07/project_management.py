"""
Project Management System
Estimate time: 4 hours
Actual time: 
"""

import datetime
from project import Project


def main():
    """Main program for project management system."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects("projects.txt")
    print(f"Loaded {len(projects)} projects from projects.txt")
    
    menu = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""
    
    choice = ""
    while choice.upper() != "Q":
        print(menu)
        choice = input(">>> ").upper()
        
        if choice == "L":
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "S":
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "Q":
            save_option = input("Would you like to save to projects.txt? ")
            if save_option.lower() not in ["no", "n", "no, i think not."]:
                save_projects("projects.txt", projects)
                print(f"Saved {len(projects)} projects to projects.txt")
            print("Thank you for using custom-built project management software.")
        else:
            print("Invalid choice")


def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    try:
        with open(filename, "r") as file:
            # Skip the header line
            file.readline()
            for line in file:
                parts = line.strip().split("\t")
                # Create a Project object from the parts
                name = parts[0]
                start_date = parts[1]
                priority = int(parts[2])
                cost_estimate = float(parts[3])
                completion_percentage = int(parts[4])
                project = Project(name, start_date, priority, cost_estimate, completion_percentage)
                projects.append(project)
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with no projects.")
    return projects


def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, "w") as file:
        # Write the header line
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        # Write each project
        for project in projects:
            file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display projects in two groups: incomplete and completed."""
    # Sort projects by priority
    incomplete_projects = [project for project in projects if not project.is_complete()]
    completed_projects = [project for project in projects if project.is_complete()]
    
    # Sort by priority
    incomplete_projects.sort()
    completed_projects.sort()
    
    # Display incomplete projects
    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(f"  {project}")
    
    # Display completed projects
    print("Completed projects: ")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter projects by date and display them."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    try:
        # Try to parse date with different formats
        try:
            # Try with format %d/%m/%Y (4-digit year)
            filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        except ValueError:
            # Try with format %d/%m/%y (2-digit year)
            filter_date = datetime.datetime.strptime(date_string, "%d/%m/%y").date()
        
        # Filter projects that start after the given date
        filtered_projects = []
        for project in projects:
            if project.get_date_object() >= filter_date:
                filtered_projects.append(project)
        
        # Sort the filtered projects by date
        filtered_projects.sort(key=lambda project: project.get_date_object())
        
        # Display the filtered projects
        for project in filtered_projects:
            print(project)
    except ValueError:
        print("Invalid date format. Use dd/mm/yyyy or dd/mm/yy.")


if __name__ == "__main__":
    main()
