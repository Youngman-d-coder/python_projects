my_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

row = int(input("Select a row to be displayed:  "))

print(my_list[row])

num = int(input("Enter a number to add to the row:  "))
my_list[row].append(num)

print(my_list[row])
