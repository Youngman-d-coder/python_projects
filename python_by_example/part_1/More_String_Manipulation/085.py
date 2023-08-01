name = input("Enter your name:  ")
vowels = ['a','e','i','o','u']
count = 0

for i in name:
    for x in vowels:
        if (i == x):
            count += 1

print(f"you have {count} vowels in your name")
