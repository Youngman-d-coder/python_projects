import random, turtle

bob = turtle.Turtle()

for i in range(8):
    colour = random.choice(['red', 'purple', 'green', 'grey', 'orange', 'gold'])
    bob.color(colour)
    bob.fd(150)
    bob.lt(360/8)

turtle.mainloop()
