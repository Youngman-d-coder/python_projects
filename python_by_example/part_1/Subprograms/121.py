def create_list():
    new_list = []
    print("List completed successfully!")
    return new_list

def checker():
    if new_list == True:
        create_list()
        return new_list
    else:
        print("List already exists!")

def view_list_content():
    for i in new_list:
        print(f"{i}", end=", ")
    print()

def add_to_list():
    num = int(input("How many names do yo you want to enter into list:  "))
    for i in range(num):
        new_member = input("Enter new list member:  ").lower()
        new_list.append(new_member)
    print("List completed successfully!")
    return new_list

def remove_from_list():
    del_member = input("Enter member to be deleted:  ").lower()
    del_member_index = new_list.index(del_member)
    del new_list[del_member_index]
    print("deleted successfully!")
    return new_list

def change_in_list():
    change_index = int(input("Enter index of member to be changed:  "))
    new_change = input("Enter new member:  ").lower()
    new_list[change_index] = new_change
    print("List completed successfully!")
    return new_list

def menu():
    print("""
        1. create empty list.
        2. check for list.
        3. View list
        4. edit or add to list.
        5. delete from list.
        6. close/end program
    """)

def main():
    while True:
        menu()
        choice = int(input("Select from the menu:  "))
        if choice == 1:
            create_list()
        elif choice == 2:
            checker()
        elif choice == 3:
            view_list_content()
        elif choice == 4:
            new_choice = int(input("enter 1 to edit list or 2 to add to list:  "))
            if new_choice == 1:
                change_in_list()
            elif new_choice == 2:
                add_to_list()
            else:
                print("invalid option")
        elif choice == 5:
            remove_from_list()
        elif choice == 6:
            break
        else:
            print("invalid option")

new_list = []
main()