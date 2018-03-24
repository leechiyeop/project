import turtle as t
import random as r

def up() :
	t.left(1)

def down() :
	t.right(1)

def launch() :
	#1. 포물선 생성-땅에 닿을 때까지 돌진 2. 타깃이랑 거북이 거리 차이 확인 3. 태초마을
	#타겟은 랜덤으로 50-150
	angle = t.heading()
	
	while t.ycor() > 0 :
		t.fd(20)
		t.right(5)
	
	dis = t.distance(target, 0)
	t.sety(r.randint(10, 100))
	if dis <= 25 :
		t.pencolor('blue')
		t.write('Bingo!!', False, "center", ("",15))
		t.pencolor('black')
	else :
		t.pencolor('red')
		t.write('Daaaammmmmmmmmmm!!!!!!!', False, "center", ("", 15))
		t.pencolor('black')
	t.goto(-200,10)
	t.setheading(angle)

def setting() :
	t.goto(-300,0)
	t.down()
	t.goto(300,0)
	ta=r.randint(50,150)
	t.up()
	t.goto(ta-25,0)
	t.down()
	t.pencolor('red')
	t.pensize(5)
	t.goto(ta+25,0)
	t.up()
	t.goto(-200,10)
	t.pencolor('black')
	return ta

t.onkeypress(setting, 'Escape')
target = setting()
t.onkeypress(up,'Up')
t.onkeypress(down, 'Down')
t.onkeypress(launch, 'space')

t.listen()

t.mainloop()

