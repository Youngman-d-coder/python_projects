food = {}

for i in range(4):
    food[i + 1] = input("Add your favourite food:  ")

print(food)

discard = int(input("Enter the index of the one you hate: "))

del food[discard]

print(sorted(food.values()))
