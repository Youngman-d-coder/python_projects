import random

score = 0
correct = 0
tries = 0

print("Please answer correctly!")

while (tries < 5):
    num_1 = random.randint(1, 1000)
    num_2 = random.randint(1, 1000)
    ans = num_1 + num_2
    print(f"{num_1} + {num_2} = ", end='')
    answer = int(input(" "))
    if (answer == ans):
        score += 20
        correct += 1
        tries += 1
    else:
        tries += 1

print(f"you answered {correct} correctly and you score is {score}%")
