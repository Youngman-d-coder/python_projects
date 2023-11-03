import csv

def menu():
    print('''
        1) Add to file
        2) view all records
        3) delete a record
        4) quit program
    ''')

def add_to_file():
    file = open("Salaries.csv", "a")
    choice = int(input("How many name do you want to enter:  "))
    for i in range(choice):
        name = input("\nEnter name of employee:  ").lower()
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

def delete_a_record():
    file = list(csv.reader(open("Salaries.csv")))
    tmp = []

    for row in file:
        tmp.append(row)

    for i in tmp:
        print(i)

    del_member = int(input("Enter member index to be deleted:  "))
    del tmp[del_member]
    print("deleted successfully!")
    return tmp

def add_list_to_file(tmp):
    file = open("Salaries.csv","w")
    x = 0
    for row in tmp:
        newRec = tmp[x][0] + "," + tmp[x][1] + "\n"
        file.write(newRec)
        x += 1

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
            cond == add_list_to_file(delete_a_record())
        elif choice == 4:
            cond = quit_program()
        else:
            print("Invalid Option")

main()