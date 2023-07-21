subjects = ["English","Mathematics","Biology","Chemistry","Physics","Social Studies","Civic Education","Geography","Computer Science","Physical and Health Education","Animal Husbandry"]

n = 1
while (n < 12):
    for subject in subjects:
        print(f" {n} : {subject}")
        n += 1
print('\n')

for i in range(30):
    print("*", end="")
sub = input(" \nEnter hated subject:  ").capitalize()
for i in range(30):
    print("*", end="")

ind = subjects.index(sub)

print('\n')
del subjects[ind]
i
m = 1
while (m < 11):
    for subject in subjects:
        print(f" {m} : {subject}")
        m += 1
