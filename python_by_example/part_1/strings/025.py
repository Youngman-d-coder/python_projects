f_name = input("Enter you first name:  ")

if (len(f_name) > 5):
    print(f_name.lower())
else:
    l_name = input("Enter your surname:  ")
    fullname = f_name + l_name
    print(fullname.upper())
