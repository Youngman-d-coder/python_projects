invitees = []

for i in range(3):
    name = input("Enter the name of invitee: ")
    invitees.append(name)

ask = input("Do you want to add another person? (y/n): ").lower()

while (True):
    if (ask == 'y'):
        name = input("Enter the name of invitee: ")
        invitees.append(name)
        ask = input("Do you want to add another person? (y/n): ").lower()
    elif (ask == 'n'):
        for i in invitees:
            print(i)
        ask_1 = input("Enter a name from the list: ")
        ind = invitees.index(ask_1)
        print(ind)
        do = input("Do you still want them in the party? (y/n) ")
        if (do == 'n'):
            invitees.remove(ask_1)
        for i in invitees:
            print(i)
        break

