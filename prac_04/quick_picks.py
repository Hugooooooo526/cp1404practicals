import random
a = []
user_choice_num = int(input("How many quick picks? "))

for i in range(user_choice_num):
    #row
    a = []
    for j in range(6):
        b = random.randint(1,45)
        a.append(b)  # record all random num in list
    a.sort()  # sort the list
    # Using format string to right-align each number
    print(" ".join([f"{num:>2}" for num in a]))  # print in order way with right alignment
    #1. fprint 可以用不同符号代替括号 当符号冲突时。2.fprint 左右对齐的输出需要在"{}"中表示 而不是"{}"外。3.