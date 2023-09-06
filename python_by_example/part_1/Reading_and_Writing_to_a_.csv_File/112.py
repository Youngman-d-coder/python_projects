import csv

file = open("Books.csv", "a")

new_line = input("Enter new data in format (Title, Author, Date):  ")
file.write(str(new_line + "\n"))

file.close()

file = open("Books.csv", "r")
for line in file:
    print(line)
file.close()
