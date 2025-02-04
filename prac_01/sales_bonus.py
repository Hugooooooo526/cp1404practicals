"""
pseudocode:
get sales
while sales >= 0
    calculate bonus (this line is intentionally incomplete pseudocode)
    print bonus
    get sales
do next thing
"""

sales = float(input("Enter sales: $"))
while(sales >= 0):
    # 负数的时候是结束
    if sales < 1000:
        bonus_rate = 0.1

    else:
        bonus_rate = 0.15
    
    bonus = sales * bonus_rate

    print(f"Bonus: ${bonus:.2f}")

    sales = float(input("Enter sales: $"))

print("End of program")


