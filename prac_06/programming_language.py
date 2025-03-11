class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        
    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
    
# Python, Dynamic Typing, Reflection=True, First appeared in 1991