import random

while (True):
    ran_col = random.choice(['red', 'green', 'pink', 'orange', 'blue'])
    cho_col = input("Guess the colour:  ").lower()
    if (cho_col == ran_col):
        print("Well done")
        break
    elif (cho_col != ran_col and ran_col == 'green'):
        print("you reek of GREEN disgust")
        cho_col = input("Guess the colour:  ").lower()
    elif (cho_col != ran_col and ran_col == 'red'):
        print("Looking RED with anger will solve it")
        cho_col = input("Guess the colour:  ").lower()
    elif (cho_col != ran_col and ran_col == 'blue'):
        print("BLUE envy is ugly")
        cho_col = input("Guess the colour:  ").lower()
    elif (cho_col != ran_col and ran_col == 'orange'):
        print("try to be as sweet as ORANGE")
        cho_col = input("Guess the colour:  ").lower()
    elif (cho_col != ran_col and ran_col == 'pink'):
        print("PINK is the new cool")
        cho_col = input("Guess the colour:  ").lower()
