#QUESTION: Determine is a fruit is ripe, overripe or unripe base on its color. Example - Banana: Green(unripe), Yellow(ripe), Brown(overripe)

fruit ="Banana"
color = "Red"

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")
    else:
        print("Wasted")
else:
    print("Other fruits are not applicable right now.")