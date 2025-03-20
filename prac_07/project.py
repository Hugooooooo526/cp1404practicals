"""
Project class implementation
Estimate time: 2 hours
Actual time: 
"""

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
