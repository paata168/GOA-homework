from turtle import *


#we want to paint a house

#step 1 : draw a squeare 
speed(30)
width(7)
color("green")
forward(200)
left(90)
 
forward(200)
left(90)

forward(200)
left(90)
 
forward(200)
left(90)
#and of squeare

#drawing a door

forward(70)
color("red")
begin_fill()
left(90)
forward(120)  # height of the door
right(90)
forward(50)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()
color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("blue")
begin_fill()
penup()
goto(60, 150 )
pendown()

right(60)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

begin_fill()
penup()
goto(170 , 190)
pendown()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()


exitonclick()