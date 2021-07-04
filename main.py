'''project by Mr_Myster
Check out our yt channel 
link in readme file'''

import turtle   #importing turtle mofdule

colors = ['red', 'yellow', 'green', 'purple', 'orange', 'blue']     #setting the colors


t = turtle.Pen()
t.shape('turtle')       #setting the shape of the pen as turtle
turtle.bgcolor('black')     #setting the bg color as black
for x in range(200):
    t.pencolor(colors[x%6])     #using the different colors form color
    t.width(x//20)
    t.forward(x)
    t.left(50)
    
# youtube link is availabe in read me file
