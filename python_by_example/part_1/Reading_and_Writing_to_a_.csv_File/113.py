import csv

file = open("Books.csv", "a")
num = int(input("How man data do you want to record:  "))
for i in range(num):
    title = input("Enter Title:  ")
    author = input("Enter Author:  ")
    year = input("Enter Year:  ")
    line = f"{title}, {author}, {year}\n"
    file.write(line)
file.close()

file = open("Books.csv", "r")
ques_author = input("Which author are you looking for:  ")
for line in file:
    count = 0
    if ques_author in line:
        count += 1
        print(line)
    
if count == 0:
    print("Author not found in list")
file.close()
