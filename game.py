import turtle
wn=turtle.Screen()
wn.bgcolor("white")
ibrahim=turtle.Turtle()
ibrahim.shape("turtle")
ibrahim.speed(5)

   
ashik=turtle.Turtle()
ashik.color("blue")
ashik.shape()
dist=20 
ashik.speed(5)
for i in range(20):
    ashik.forward(dist)
    ashik.left(45)
    ashik.forward(dist)
    dist+=5
    ibrahim.circle(dist)
wn.exitonclick()
