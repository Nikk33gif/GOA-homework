from turtle import*
speed(30)
color("black")
width(10)

color("yellow")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()

#door
forward(70)
color("blue")
begin_fill()
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()


penup()
goto(200,200)
pendown()
color("blue")

begin_fill()
right(150)
forward(200)
left (120)
forward(200)
end_fill()

color("black")
begin_fill()
left(120)
forward(60)
right (90) 
forward(60)
right (90)
forward(60)
end_fill()


penup()
goto(200,200)
pendown()

begin_fill()
forward(60)
left(90)
forward(60)
left(90)
forward(60)
end_fill()




exitonclick()


