"""
Estimate time: 20 minutes
Actual time: 14 minutes
"""

import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from guitar import Guitar

def main():
    """Demo test code to show how to use car class."""
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(guitar)
    another_guitar = Guitar("Another Guitar",2013,1000)
    print(f"{guitar.name} get_age() - Expected 100. Got {guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age()}")      
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")
    
main()