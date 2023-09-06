import csv

file = open("Books.csv", "w")

line = "To Kill A Mockingbird, Harper Lee, 1960\n"
file.write(str(line))

line = "A Brief History of Time, Stephen Hawking, 1988\n"
file.write(str(line))

line = "The Great Gatsby, F. Scott Fitzgeralg, 1922\n"
file.write(str(line))

line = "The Man Who Mistook His Wife for a Hat, Olive Sacks, 1985\n"
file.write(str(line))

line = "Pride and Prejudice, Jane Austen, 1813\n"
file.write(str(line))

file.close()
