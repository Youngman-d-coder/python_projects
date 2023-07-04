ask = input("Which direction do you want to count (up/down) :  ")

if (ask == 'up'):
    ask = int(input("Enter the top number:  "))
    for i in range(1, ask + 1):
        print(i)
elif (ask == 'down'):
    ask = int(input("Enter a number below 20:  "))
    for i in range(20, ask -1, -1):
        print(i)
else:
    print("I don't understand")
