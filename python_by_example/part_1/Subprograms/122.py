import csv

def menu():
    print('''
        1) Add to file
        2) view all records
        3) quit program
    ''')

def add_to_file():
    file = open("Salaries.csv", "a")
    choice = int(input("How many name do you want to enter:  "))
    for i in range(choice):
        name = input("\nEnter name of employee:  ")
        salary = int(input("How much salary do they earn:  "))
        new_record = ("{}, {}\n".format(name, str(salary)))

        file.write(str(new_record))
    print("\nList Successfully updated!")
    file.close()
    return True

def view_all_records():
    file = open("Salaries.csv", "r")
    for row in file:
        print(row)
    file.close()
    return True

def quit_program():
    return False

def main():
    cond = True
    while cond:
        menu()
        choice = int(input("Please select from the above menu:  "))
        if choice == 1:
            cond = add_to_file()
        elif choice == 2:
            cond = view_all_records()
        elif choice == 3:
            cond = quit_program()
        else:
            print("Invalid Option")

main()