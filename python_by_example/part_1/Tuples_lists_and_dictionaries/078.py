tv_prog = ['Ben 10', 'avatar', 'Naruto', 'Atomic Betty']

for prog in tv_prog:
    print(prog)

new_prog = input("Which new programme do you want to add: ")
position = int(input("Enter the position of the programme in the list: "))

tv_prog.insert(position, new_prog)

for prog in tv_prog:
    print(prog)
