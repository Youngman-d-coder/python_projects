import turtle

bob = turtle.Turtle()

bob.penup()
bob.rt(180)
bob.fd(200)
bob.rt(180)
bob.pendown()

for i in range(5):
    bob.fd(100)
    bob.rt(360/4)

bob.penup()
bob.lt(90)
bob.fd(50)
bob.pendown()

for i in range(5):
    bob.fd(100)
    bob.rt(360/4)

bob.penup()
bob.lt(90)
bob.fd(50)
bob.pendown()

for i in range(5):
    bob.fd(100)
    bob.rt(360/4)


turtle.mainloop()
