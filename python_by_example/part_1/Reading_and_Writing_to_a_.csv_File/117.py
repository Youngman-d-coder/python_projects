import csv
import random

print("""
        Hello, Welcome to my python random maths quiz,
        Please take your time to answer all questions,
        goodluck!
        """)

name = input("Before we begin, please enter your name:  ")
userid = int(input("Enter user id:  "))

data = []
score = 0
for n in range(5):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    z = random.choice(['+', '-', '/', '*', '%'])
    question = f"{x} {z} {y}"
    user_ans = int(input(f"{question} = "))
    if z == '+':
        sys_ans = x + y
    elif z == '-':
        sys_ans = x - y
    elif z == '/':
        sys_ans = x / y
    elif z == '*':
        sys_ans = x * y
    elif z == '%':
        sys_ans = x % y

    if user_ans == sys_ans:
        score += 20

    data.append([name, question, user_ans, sys_ans, score])

with open("Exam.csv", "a", newline='') as file:
    writer = csv.writer(file)
    
    if file.tell() == 0:
        writer.writerow(["Name", "Question", "User Answer", "System Answer", "Score"])
    
    for row in data:
        writer.writerow(row)
