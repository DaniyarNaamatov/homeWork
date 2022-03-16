import turtle
screen = turtle.Screen()
draw = turtle.Turtle()
screen.bgcolor("black")
draw.pencolor("red")
draw.pensize(3)
draw1 = 0
draw2 = 0
draw.speed(100)
draw.goto(1, 200)
draw.pendown()

while True:

    draw.forward(draw1)
    draw.right(draw2)
    draw1 += 3
    draw2 += 1

    if draw2 == 210:
        break