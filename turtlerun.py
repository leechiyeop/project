#모듈가져오기
import turtle as t
import random as r
devil = t.Turtle()
feed = t.Turtle()

#함수생성
def turnup() :
	t.setheading(90)
def turndown() :
	t.setheading(270)
def turnright() :
	t.setheading(0)
def turnleft() :
	t.setheading(180)

#악당
devil.shape('turtle')
devil.up()
devil.speed(0)
devil.color('red')
devil.goto(r.randint(-229, 229), r.randint(-229, 229))

#먹이
feed.shape('circle')
feed.up()
feed.goto(r.randint(-229, 229), r.randint(-229, 229))

#주인공
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
t.goto(0,0)

#마무리
t.listen()
t.mainloop()
