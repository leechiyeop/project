#모듈가져오기
import turtle as t
import random as r
devil = t.Turtle()

feed = t.Turtle()

t.title('Turtle Run')

score = 0
playing = False

#함수생성
def turnup() :
	t.setheading(90)
def turndown() :
	t.setheading(270)
def turnright() :
	t.setheading(0)
def turnleft() :
	t.setheading(180)
def start() :
	global playing
	if playing == False : 
		playing = True
		t.clear()
		play()
		
def play() :
	global playing
	global score
	t.fd(20)
	ang = devil.towards(t.pos())
	devil.setheading(ang)
	sd=9
	if score%50==0 :
		sd += (score/50)+1
	if sd> 19: sd = 19	
	devil.fd(sd)
		
	if t.distance(feed)<15 :
		feed.goto(r.randint(-229,229), r.randint(-229,229))
		score+=50
		t.write(score)
		
	if t.distance(devil)>10 :
		t.ontimer(play,50)
	
	if t.distance(devil)<10 :
		message('GAME OVER', 'SCORE IS '+str(score))
		t.goto(0,0)
		score = 0
		playing= False
def message(m1, m2) :
	t.up()
	t.goto(0,100)
	t.write(m1, False, 'center', ('', 20))
	t.goto(0,-100)
	t.write(m2, False, 'center', ('',9))
message('START GAME', 'press space to start')

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
feed.color('yellow')

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
t.onkeypress(start, 'space')
t.goto(0,0)

#마무리
t.listen()
t.mainloop()
