"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

"""
当前，该程序要求您以大写字母输入州名（“qld” 不起作用）。更改程序，使小写输入也能显示州名。（有两个地方可以添加字符串方法。）

编写一个循环，将所有状态和名称按照字符串格式整齐地排列在一起打印出来，例如：

NSW is New South Wales
QLD is Queensland
NT  is Northern Territory
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
code_to_name = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

for code, name in code_to_name.items():
    print(f"{code} is {name}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in code_to_name:
        print(f"{state_code} is {code_to_name[state_code]}")
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()