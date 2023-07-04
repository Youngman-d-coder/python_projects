count = 0

while (True):
    ask = input("Do you want to invite someone to the party? (y/n):  ")

    if (ask == 'y'):
        invitee = input("Enter name of invitee:  ")
        print(f"{invitee} has been invited")
        count += 1
    elif (ask == 'n'):
        print(f"you invited {count} people")
        break
    else:
        print("Invalid input")
