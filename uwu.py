import turtle
pen=turtle.Turtle()

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(120)
    curve()
    pen.left(120)
    curve()
    pen.forward(120)
    pen.end_fill()
def txt():
    pen.up()
    pen.setpos(-60,90)
    pen.down()
    pen.color('white')
    pen.write('hey lol', font=("yesova",14))   

heart()
txt()
pen.ht()    
