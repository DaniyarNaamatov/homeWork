import turtle
screen = turtle.Screen()
draw = turtle.Turtle()
screen.bgcolor("black")
draw.pencolor("red")
draw.pensize(1)
coor1= 0
coor2 = 0
draw.speed(100)
draw.goto(1, 200)
draw.pendown()

while True:

    draw.forward(coor1)
    draw.right(coor2)
    coor1 += 3
    coor2 += 1

    if coor2 == 210:
        break