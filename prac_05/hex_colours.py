"""
Create a program that allows you to look up hexadecimal color codes, such as those found at http://www.color-hex.com/color-names.html.

Using a constant dictionary containing approximately 10 color names, write a program that allows the user to input a name and get the code, for example, inputting AliceBlue (or aliceblue - making it case-insensitive) should display #f0f8ff.

Entering an invalid color name should not cause the program to crash.
Allow the user to input names until an empty name is entered to stop the loop.

"""

# Using a constant dictionary containing approximately 10 color names
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

# Writing a program that allows the user to input a name and get the code
colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    if colour_name in hex_colours:
        print(f"{colour_name} is {hex_colours[colour_name]}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()