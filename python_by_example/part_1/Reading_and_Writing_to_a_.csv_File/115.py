import csv

file = open("Books.csv", "r")

x = 0
for line in file:
	line = "({}) {}".format(str(x), line)
	print(line)
	x += 1
file.close()
