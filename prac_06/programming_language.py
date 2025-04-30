class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        
    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
    
    def is_dynamic(self):
        #  The data is already inside the object, so you don't need to tell the object its own data.
        return self.typing == "Dynamic"
    
# Python, Dynamic Typing, Reflection=True, First appeared in 1991