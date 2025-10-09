from turtle import Turtle, Screen
import turtle

timmy = Turtle()

for x in range(3, 10):
    for y in range(0, x):
        timmy.forward(100)
        timmy.right(360 / x)



screen = Screen()



screen.screensize(canvwidth=700, canvheight=500, bg="lightblue")

turtle.done()

