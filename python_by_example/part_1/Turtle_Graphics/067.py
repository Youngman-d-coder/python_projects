import turtle

bob = turtle.Turtle()

for i in range(10):
    for x in range(8):
        bob.fd(100)
        bob.rt(360/8)
    bob.rt(36)

turtle.mainloop()
