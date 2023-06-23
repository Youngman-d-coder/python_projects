weather1 = input("Is it raining:  ").lower()

if (weather1 == "yes"):
    weather2 = input("Is it windy:  ")

    if (weather2 == "yes"):
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")
