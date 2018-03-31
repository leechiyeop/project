import turtle as t

t.setup(500,500)
t.shape('turtle')
t.color('white')
t.bgcolor('gray')
t.speed(0)
t.up()
t.onkeypress(turnup,'Up')
t.onkeypress(turndown, 'Down')
t.onkeypress(turnleft, 'Left')
t.onkeypress(turnright, 'Right')

def turnup() :
	t.setheading(90)
def turndown() :
	t.setheading(270)
def turnright() :
	t.setheading(0)
def turnleft() :
	t.setheading(180)

t.listen()
t.mainloop()
