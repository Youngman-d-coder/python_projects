import random

def high_low():
    h = int(input("Enter a high number"))
    l = int(input("Enter a low number"))
    comp_num = random.randint(l, h)
    return comp_num

def inst():
    print("I am thinking of a number, ")
    guess = int(input("Guess the number:  "))
    return guess

def checker(computer, user):
    if computer == user:
        print("Correct, you win!")
        return False
    elif computer > user:
        print("Incorrect, Your guess is too low")
        return True
    elif computer < user:
        print("Incorrect, Your guess is too high")
        return True
    else:
        print("Invalid Input, Try again!")
        return True

def main():
    comp_num = high_low()
    user = inst()
    
    while (checker(comp_num, user)):
        user = inst()
        
main()