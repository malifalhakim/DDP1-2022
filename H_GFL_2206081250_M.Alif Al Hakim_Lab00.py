from re import T
import turtle

turtle.hideturtle()

turtle.shape("turtle")
turtle.penup()
turtle.goto(-250,160)

turtle.pendown()
turtle.color("blue")
turtle.begin_fill() 

turtle.forward(200)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(300)

turtle.end_fill()



turtle.right(270)

turtle.penup()
turtle.goto(-17,160)

turtle.pendown()
turtle.color("red")
turtle.begin_fill()

turtle.backward(200)
turtle.right(270)
turtle.forward(50)
turtle.right(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(175)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(175)

turtle.end_fill()

turtle.exitonclick()