"""
example output:
Number of items: 3  
Price of item: 100  
Price of item: 35.56  
Price of item: 3.24  
Total price for 3 items is $124.92
"""

number_of_items = int(input("Enter the number of items: "))

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Enter the number of items: "))

total_price = 0 
for i in range(number_of_items):
    price = float(input("Enter the price of item: $"))
    total_price += price
if total_price > 100:
    total_price *= 0.9
print(f"{number_of_items} items total price is ${total_price:.2f}")
