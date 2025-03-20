"""
Project class implementation
Estimate time: 2 hours
Actual time: 2.5 hours
"""

import datetime


class Project:
    """Represent a project with attributes."""

    def __init__(self, name="", start_date="", priority=0, cost_estimate=0.0, completion_percentage=0):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of a Project."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"
    
    def __lt__(self, other):
        """Compare Projects based on priority."""
        return self.priority < other.priority
    
    def is_complete(self):
        """Check if project is complete based on completion percentage."""
        return self.completion_percentage == 100
    
    def update_completion(self, new_percentage):
        """Update the completion percentage of the project."""
        self.completion_percentage = new_percentage
    
    def update_priority(self, new_priority):
        """Update the priority of the project."""
        self.priority = new_priority
    
    def get_date_object(self):
        """Convert the start_date string to a datetime object."""
        try:
            # Try to parse with 4-digit year format
            return datetime.datetime.strptime(self.start_date, "%d/%m/%Y").date()
        except ValueError:
            # Try to parse with 2-digit year format
            return datetime.datetime.strptime(self.start_date, "%d/%m/%y").date()
    
    def days_till_start(self):
        """Calculate the number of days until the project starts from today."""
        project_date = self.get_date_object()
        today = datetime.date.today()
        return (project_date - today).days
