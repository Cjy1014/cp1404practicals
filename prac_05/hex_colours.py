COLOR_TO_CODE = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}

color_name = input("Enter a color name: ").lower()
while color_name != "":
    try:
        print(f"{color_name.capitalize()} is {COLOR_TO_CODE[color_name]}")
    except KeyError:
        print("Invalid color name")

    color_name = input("Enter a color name: ").lower()