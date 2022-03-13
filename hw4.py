import turtle
screen = turtle.Screen()
drawer = turtle.Turtle()
screen.bgcolor("black")
drawer.pencolor("dark green")
drawer.pensize(3)
drawer1 = 0
drawer2 = 0
drawer.speed(0)
drawer.goto(0, 200)
drawer.pendown()

while True:

    drawer.forward(drawer1)
    drawer.right(drawer2)
    drawer1 += 3
    drawer2 += 1

    if drawer2 == 210:
        break

drawer.ht()
screen.mainloop()