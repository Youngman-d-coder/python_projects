num_1 = int(input("Enter a number:  "))
num_2 = int(input("Enter a number:  "))

ans = num_1 + num_2

while True:
    ask = input("Do you want to add another number? (Y/N):  ").lower()
    if (ask == 'y'):
        num_3 = int(input("Enter a number:  "))
        ans += num_3
    else:
        break

print(ans)
