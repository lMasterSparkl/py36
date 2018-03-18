from turtle import *
def numb(a,i):
    if a==0:
        penup()
        goto(100*(i+0.9),0)
        pendown()
        backward(80)
        left(90)
        forward(160)
        right(90)
        forward(80)
        right(90)
        forward(160)

color("blue")
pensize(5)
#hideturtle()
speed(5)
a=0
numb(a,0)

