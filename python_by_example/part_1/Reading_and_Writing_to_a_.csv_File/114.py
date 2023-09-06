import csv

start = int(input("Enter starting year: "))
end = int(input("Enter ending year:  "))

file = open("Books.csv", "r")

for line in file:
    for year in range(start, end):
        if str(year) in line:
            print(line)
file.close()

"""
import csv

start = int(input("Enter starting year: "))
end = int(input("Enter ending year:  "))

file = list(csv.reader(open("Books.csv")))
tmp = []
for line in file:
    tmp.append(line)

x = 0
for line in tmp:
	if int(tmp[x] [2]) >= start and int(tmp[x] [2]) <= end:
		print(tmp[x])
	x = x + 1
"""
