first_name = input("Enter your first name:  ")
length_of_fn = len(first_name)
print(f"Your first name is {length_of_fn} characters long")

last_name = input("Enter your surname:  ")
length_of_ln = len(last_name)
print(f"Your first name is {length_of_ln} characters long")

full_name = last_name + ' ' + first_name
print(full_name)
length_of_fln = len(full_name)
print(f"Your full name is {length_of_fln} characters long")
