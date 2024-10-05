import turtle
def start_spel():
    turtle.onkey(None,'space')
    for i in range(4):
        elsa.forward(60)
        elsa.right(90)
        elsa.backward(100)
    for n in range(18):
        elsa.forward(50)
        elsa.stamp()
        elsa.left(20)
elsa = turtle.Turtle()
screen = turtle.Screen()
elsa.color("blue")
tekst_turtle=turtle.Turtle()
tekst_turtle.penup()
tekst_turtle.goto(-200,200)
tekst_turtle.pendown()
tekst_turtle.write('',align='center', font=('Arial',16,'bold'))
tekst_turtle.write('druk op x om de pen aan de zetten',align='center', font=('Arial',16,'bold'))
tekst_turtle.hideturtle()
def doeh():
    tekst_turtle.clear()
    for i in range(1):
        elsa.forward(60)
        elsa.heading(0)
        elsa.backward(60)
        elsa.forward(90)
turtle.onkey(doeh,'h')
turtle.onkey(start_spel,'space')
turtle.onkey(elsa.penup,'d')
turtle.onkey(elsa.pendown,'x')
turtle.onkey(elsa.clear,'l')
screen.onclick(elsa.goto)
turtle.listen()
turtle.mainloop()
def doeh():
    tekst_turtle.clear()
    
    for i in range(1):
        elsa.forward(60)
        elsa.heading(90)
        elsa.backward(60)
        elsa.forward(90)
turtle.done()