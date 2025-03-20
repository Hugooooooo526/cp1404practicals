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


if __name__ == "__main__":
    main()
