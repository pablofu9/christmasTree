
import turtle


width = 500
height = 500

#CREAMOS EL SCREEN
screen = turtle.Screen()
screen.setup(width, height)
screen.title('Mi arbol ded navidad')

screen.bgcolor("blue")

#CREAMOS EL PEN
pencil = turtle.Pen()
pencil.speed(0)


pencil.up()
pencil.setposition(-60, 100)
pencil.down()
pencil.fillcolor('green')
pencil.begin_fill()
pencil.fd(120)
pencil.lt(130)
pencil.fd(95)
pencil.lt(100)
pencil.fd(95)
pencil.end_fill()

# Middle trapezoid
pencil.setx(-35)
pencil.fillcolor('green')
pencil.begin_fill()
pencil.fd(100)
pencil.lt(130)
pencil.fd(200)
pencil.lt(130)
pencil.fd(100)
pencil.end_fill()


pencil.up()
pencil.setposition(-45, 24)
pencil.down()
pencil.fillcolor('green')
pencil.begin_fill()
pencil.lt(100)
pencil.fd(130)
pencil.lt(130)
pencil.fd(260)
pencil.lt(130)
pencil.fd(130)
pencil.end_fill()


pencil.up()
pencil.setposition(-30, -75)
pencil.down()
pencil.fillcolor('brown')
pencil.begin_fill()
pencil.lt(140)
pencil.fd(50)
pencil.lt(90)
pencil.fd(60)
pencil.lt(90)
pencil.fd(50)
pencil.end_fill()

# Star on the top
pencil.up()
pencil.setposition(-30, 190)
pencil.rt(90)
pencil.down()
pencil.fillcolor('yellow')
pencil.begin_fill()
for i in range(5):
    pencil.fd(60)
    pencil.rt(144)
pencil.end_fill()
pencil.hideturtle()

colors = ['red', 'yellow', 'cyan']

tier1 = turtle.Pen()
tier2 = turtle.Pen()
tier3 = turtle.Pen()

tier1.up()
tier1.setposition(0, -20)
tier1.down()
tier1.hideturtle()

tier2.up()
tier2.setposition(0, 60)
tier2.down()
tier2.hideturtle()

tier3.up()
tier3.setposition(0, 130)
tier3.down()
tier3.hideturtle()


m = 0
while True:
    tier1.dot(20, colors[m % 3])  # 0,1,2,0,1,2,0,1,2,...
    tier2.dot(20, colors[(m + 1) % 3])  # 1,2,0,1,2,0,1,2,0,...
    tier3.dot(20, colors[(m + 2) % 3])  # 2,0,1,2,0,1,2,0,1,...
    m = m + 1
