import random as r

def making_questions() :
	a = r.randint(1,32)
	b = r.randint(1,3)
	c = r.randint(4,93)
	
	if b == 1 : buho = '+'
	elif b == 2 : buho = '-'
	else : buho = '*'
	
	ques = str(a)+' '+buho+' '+str(c)
	
	return ques

for a in range(5) :
	q = making_questions()
	
	ans = input(q+' = ')

	if eval(q) == int(ans) : print("Correct!!")
	else : print("Wrong!!")
