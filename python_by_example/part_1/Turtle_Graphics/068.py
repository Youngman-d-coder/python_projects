import turtle, random

bob = turtle.Turtle()

num = random.randint(1, 100)

for i in range(num):
    a = random.randint(1, 100)
    for x in range(a):
        b = random.randint(1, 200)
        bob.fd(b)
        bob.rt(a)
    d = random.randint(1, 100)
    bob.rt(d)

turtle.mainloop()
