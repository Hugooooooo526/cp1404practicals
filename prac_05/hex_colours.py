"""
根据上面的州名示例程序，创建一个程序，让你可以查找十六进制颜色代码，如 http://www.color-hex.com/color-names.html上的代码

使用一个包含大约 10 个颜色名称的常量字典并编写一个程序，允许用户输入名称并获取代码，例如输入 AliceBlue（或aliceblue- 使其与大小写无关）应该显示#f0f8ff。

输入无效的颜色名称不应导致程序崩溃。
允许用户输入名称，直到输入空白名称以停止循环。

"""

hex_colours = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff",
}

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    if colour_name in hex_colours:
        print(f"{colour_name} is {hex_colours[colour_name]}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()