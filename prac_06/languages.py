"""
Estimate time: 30 minutes
Actual time: 20 minutes
"""

# Dynamically import Car class
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from programming_language import ProgrammingLanguage

def main():
    """Demo test code to show how to use car class."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    
    # Create a list to store programming language instances
    languages = [python, ruby, visual_basic]
    
    # Print all dynamically typed languages
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)
    
main()    
    
