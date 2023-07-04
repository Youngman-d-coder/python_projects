invitees_num = int(input("Enter the number of people you want to invite to a party:  "))

if (invitees_num < 10):
    for i in range(invitees_num):
        invitees = input("Enter name of invitee: ")
        print(f"{invitees} has been invited")
else:
    print("Too many people")
