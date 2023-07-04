total = 0

for quest in range(5):
    num = int(input("Enter a number:  "))
    ask = input("Do you want to add this number (y/n):  ").lower()
    if (ask == 'y'):
        total += num
    else:
        total = total

print(total)
