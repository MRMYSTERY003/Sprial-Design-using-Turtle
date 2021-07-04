import turtle

colors = ['red', 'yellow', 'green', 'purple', 'orange', 'blue']
t = turtle.Pen()
t.shape('turtle')
turtle.bgcolor('black')
for x in range(200):
    t.pencolor(colors[x%6])
    t.width(x//20)
    t.forward(x)
    t.left(50)
    
