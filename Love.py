import turtle

s= turtle.Screen().bgcolor('black')
t = turtle.Turtle()
t.speed(0)
t.width(5)

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)
def heart():
    t.color('red','red')
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()
def txt():
    t.up()
    t.setpos(-57, 95)
    t.down()
    t.color('white')
    t.write("Bucin Anj*ng", font=(
        "Verdana", 12, "bold"))
heart()
txt()
t.ht() 
turtle.exitonclick()
