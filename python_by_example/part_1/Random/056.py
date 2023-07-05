import random

num = random.randint(1, 10)

guess = int(input("Enter a number:  "))

while (True):
    if (guess == num):
        print("Correct guess")
        break
    else:
        print("Incorrect guess!")
        guess = int(input("Enter a number:  "))
