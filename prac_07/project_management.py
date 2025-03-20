"""
Project Management System
Estimate time: 4 hours
Actual time: 
"""

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
        elif choice == "D":
            display_projects(projects)
        elif choice == "Q":
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


def display_projects(projects):
    """Display projects in two groups: incomplete and completed."""
    # Sort projects by priority
    incomplete_projects = [project for project in projects if not project.is_complete()]
    completed_projects = [project for project in projects if project.is_complete()]
    
    # Sort by priority (will add this feature later)
    
    # Display incomplete projects
    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(f"  {project}")
    
    # Display completed projects
    print("Completed projects: ")
    for project in completed_projects:
        print(f"  {project}")


if __name__ == "__main__":
    main()
