print("""
        1) Create a new file
        2) Display the file
        3) Add a new item to the file
        Make a selection 1, 2 or 3:
        """)

num = int(input("Enter your selection:  "))
if num == 1:
    school = input("Enter a school name:  ")
    file = open("Subject.txt", "w")
    file.write(school + "\n")
    file.close()
elif num == 2:
    file = open("Subject.txt", "r")
    print(file.read())
    file.close()
elif num == 3:
    subject = input("Enter a subject name:  ")
    
    file = open("Subject.txt", "a")
    file.write(subject + "\n")
    file.close()

    file = open("Subject.txt", "r")
    print(file.read())
    file.close()
else:
    print("Invalid Input")
