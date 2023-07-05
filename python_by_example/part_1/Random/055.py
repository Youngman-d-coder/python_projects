import random

num = random.randint(1, 5)

guess = int(input("Make a guess of a number from 1 through 5:  "))

if (guess == num):
    print ("Well done")
elif (guess > num):
    print("Too high!")
    guess = int(input("Make a guess of a number from 1 through 5:  "))
    if (guess == num):
        print("Correct!")
    else:
        print("You lose")
else:
    print("Too low")
    guess = int(input("Make a guess of a number from 1 through 5:  "))
    if (guess == num):
        print("Correct!")
    else:
        print("You lose")

