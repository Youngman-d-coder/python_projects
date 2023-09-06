my_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

row = int(input("Select a row to be displayed:  "))

print(my_list[row])

column = int(input("Select a column to be displayed:  "))
print(my_list[row] [column])

ask = input("Do you want to replace the number?(y or n):  ").lower()

if ask == 'y' and ask != 'n':
    new_num = int(input("Enter new number:  "))
    my_list[row] [column] = new_num
    print(my_list[row])
elif ask != 'y' and ask == 'n':
    exit()
else:
    print("invalid Input")
