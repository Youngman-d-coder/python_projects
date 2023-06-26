from math import pi

radius = float(input("Enter radius of cylinder :  "))
depth = float(input("Enter depth of cylinder :  "))

circle_area = pi * (radius ** 2)
volume = circle_area * depth

print(round(volume, 3))