import random

choice = random.choice(['h', 't'])

guess = input("Make a guess 'h' for heads and 't' for tails:  ").lower()

if (guess == choice):
    print("You win")
else:
    print("Bad luck")
    if (choice == 'h'):
        print("The computer selected heads")
    else:
        print("The computer selected tails")
