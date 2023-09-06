file = open("Names.txt", "r")
print(file.read())
file.close()

name = input("Which name do you want out of the list:  ")
file = open("Names.txt", "r")
name = name + "\n"

for n in file:
    if n != name:
        file = open("Names2.txt", "a")
        file.write(n)
        file.close()
file.close()
