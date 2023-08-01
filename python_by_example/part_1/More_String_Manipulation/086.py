pswd_1 = input("Enter a password:  " )
pswd_2 = input("Comfirm  password:  " )

if (pswd_1 == pswd_2):
    print("Thank you")
elif (pswd_1.lower() == pswd_2.lower()):
    print("Must be in the same case")
else:
    print("Incorrect")
