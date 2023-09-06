import csv

file = list(csv.reader(open("Books.csv")))

tmp = []
for line in file:
    tmp.append(line)

num = 0
for x in range(len(tmp)):
    print("{} {}".format(num, tmp[x]))
    num += 1

for i in range(3):
    print()

row1 = int(input("Which row do you want to delete: "))
del tmp[row1]
num = 0
for x in range(len(tmp)):
    print("{} {}".format(num, tmp[x]))
    num += 1

for i in range(3):
    print()

row2 = int(input("Which row do you want to change: "))
title = input("Enter Title:  ")
author = input("Enter Author:  ")
year = input("Enter Year:  ")
tmp[row2] [0] = title
tmp[row2] [1] = author
tmp[row2] [2] = year

num = 0
for x in range(len(tmp)):
    print("{} {}".format(num, tmp[x]))
    num += 1

for i in range(3):
    print()

file = open("Books.csv", "w")
n = 0
for x in tmp:
    line = "{}, {}, {}\n".format(tmp[n][0], tmp[n][1], tmp[n][2])
    file.write(line)
    n += 1
file.close()

file = open("Books.csv", "r")
for x in file:
    print(x)
file.close()
