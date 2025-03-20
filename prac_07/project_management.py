"""
Project Management System
Estimate time: 1 hours
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
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
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


def add_new_project(projects):
    """Add a new project to the list of projects."""
    print("Let's add a new project")
    name = input("Name: ")
    
    valid_date = False
    while not valid_date:
        start_date = input("Start date (dd/mm/yy): ")
        try:
            datetime.datetime.strptime(start_date, "%d/%m/%Y")
            valid_date = True
        except ValueError:
            try:
                datetime.datetime.strptime(start_date, "%d/%m/%y")
                valid_date = True
            except ValueError:
                print("Invalid date format. Please use dd/mm/yyyy or dd/mm/yy.")
    
    valid_input = False
    while not valid_input:
        try:
            priority = int(input("Priority: "))
            valid_input = True
        except ValueError:
            print("Priority must be an integer.")
    
    valid_input = False
    while not valid_input:
        try:
            cost_string = input("Cost estimate: $")
            if cost_string.startswith('$'):
                cost_string = cost_string[1:]
            cost_estimate = float(cost_string)
            valid_input = True
        except ValueError:
            print("Cost estimate must be a valid number.")
    
    valid_input = False
    while not valid_input:
        try:
            completion_percentage = int(input("Percent complete: "))
            if 0 <= completion_percentage <= 100:
                valid_input = True
            else:
                print("Percent complete must be between 0 and 100.")
        except ValueError:
            print("Percent complete must be an integer.")
    
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)


def update_project(projects):
    """Update an existing project."""
    # Display all projects with index
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    
    # Get the project to update
    project_choice = int(input("Project choice: "))
    project = projects[project_choice]
    print(project)
    
    # Update completion percentage
    new_percentage = input("New Percentage: ")
    if new_percentage:
        project.update_completion(int(new_percentage))
    
    # Update priority
    new_priority = input("New Priority: ")
    if new_priority:
        project.update_priority(int(new_priority))


if __name__ == "__main__":
    main()
