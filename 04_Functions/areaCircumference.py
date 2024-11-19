import math

def circleStats(radius):
    print("hi")
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return area, circumference

a, b = circleStats(4)

print("area:", round(a,2),"circumference:",round(b,2))