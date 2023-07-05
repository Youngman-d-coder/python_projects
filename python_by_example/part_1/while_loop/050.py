num = int(input("Enter a number between 10 and 20"))

while (True):
    if (num < 10):
        print(""" Tool low
         Try Again """)
    elif (num > 20):
        print(""" Tool high
         Try Again """)
    else:
        print("Thank you")
        break
