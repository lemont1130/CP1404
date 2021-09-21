COLOURS_LIST = {"AliceBlue": "#f0f8ff", "antiquewhite": "#feabd7", "forestgreen": "#228b22", "floralwhite": "#fffaf0",
                "firebrick": "#b22222", "gold": "#ffd700", "gray": "#bebebe", "greenyellow": "#adff2f",
                "hotpink": "#ff69b4", "ivory": "#fffff0"}
colours = input("Enter a colour:")
while colours != "":
    if colours in COLOURS_LIST:
        print(colours,"is",COLOURS_LIST[colours])
    else:
        print("Invalid")
    colours = input("Enter a colour:")
