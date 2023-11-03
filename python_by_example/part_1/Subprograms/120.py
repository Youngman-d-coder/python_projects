import random

def msg():
    print('''
    1) Addition
    2) Subtraction
    Enter 1 or 2:
    ''')

def add_rando():
    n = random.randint(5, 20)
    m = random.randint(5, 20)
    user = int(input(f"{n} + {m} =  "))
    comp = n + m
    return user, comp

def sub_rando():
    n = random.randint(25, 50)
    m = random.randint(1, 25)
    user = int(input(f"{n} - {m} =  "))
    comp = n - m
    return user, comp

def checker(u, c):
    if u == c:
        print("Correct answer!")
    else:
        print(f"Incorrect answer, the correct is {c}")

def main():
    msg()
    choice = int(input("Your selection:  "))
    if choice == 1:
        user, comp = add_rando()
        checker(user, comp)
    elif choice == 2:
        user, comp = sub_rando()
        checker(user, comp)
    else:
        print("Invalid selection")

main()