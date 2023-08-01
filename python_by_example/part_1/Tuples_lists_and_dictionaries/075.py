num = [745, 624, 569, 298]

for i in num:
    print(i)

ask = int(input("Enter a three-digit number:  "))

if ask in num:
    print(num.index(ask))
else:
    print("That is not in the list")
