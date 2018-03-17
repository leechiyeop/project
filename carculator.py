import random as r

def making_questions() :
	a = r.randint(1,32)
	b = r.randint(1,3)
	c = r.randint(4,93)
	
	if b == 1 : buho = '+'
	elif b == 2 : buho = '-'
	else : buho = '*'
	
	ques = str(a)+' '+buho+' '+str(c)+' = '
	
	return ques

