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
        print(len(invitees))
        break

