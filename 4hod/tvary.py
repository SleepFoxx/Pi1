import turtle
from random import randrange, uniform
turtle.delay(0)

t = turtle.Turtle()
t.pencolor()
dlzkaA = randrange(0,100)
uhol = randrange(0,100)
t.penup()
t.setheading(uhol)
t.pendown()
t.pensize(6)
vyska = 800
sirka = 600
turtle.setup(900,700)

def stvorec(dlzkaA):
    xpozicia = randrange(1, sirka)
    ypozicia = randrange(1, vyska)
    t.penup()
    t.setpos(xpozicia,ypozicia)
    t.pendown()
    t.pencolor("red")
    for i in range(4):
        t.forward(dlzkaA)
        t.right(90)

def trojuholnik(dlzkaA):
    xxpozicia = randrange(1, vyska)
    yypozicia = randrange(1, sirka)
    t.penup()
    t.setpos(xxpozicia, yypozicia)
    t.pendown()
    t.pencolor("blue")
    for i in range(3):
        t.forward(dlzkaA)
        t.left(120)

pocet_trojuholnikov = randrange(1,10)
pocet_stvorcov = randrange(1,10)

for y in range(pocet_stvorcov):
    trojuholnik(dlzkaA)
    stvorec(dlzkaA)

turtle.exitonclick()
