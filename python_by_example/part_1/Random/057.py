import random

num = random.randint(1, 10)

guess = int(input("Enter a number:  "))

while (True):
    if (guess == num):
        print("Correct guess")
        break
    else:
        print("Incorrect guess!")
        if (guess > num):
            print("Too high")
            guess = int(input("Enter a number:  "))
        else:
            print("Too low")
            guess = int(input("Enter a number:  "))
