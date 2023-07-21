print(" 1) Square\n 2) Triangle\n")

num = int(input(" Enter a number: "))

if (num == 1):
    length = int(input(" Enter the length of one side: "))
    area = length ** 2
    print(f" {area}")
elif (num == 2):
    base = int(input(" Enter the base: "))
    height = int(input(" Enter the height: "))
    area = (1/2) * b * h
    print(f" {area}")
else:
    print(" Error: Invalid Input")
