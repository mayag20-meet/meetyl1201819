import turtle
import time
import random
from ball import Ball
import math

turtle.tracer(0,0)
turtle.hideturtle()
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()//2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()//2

my_ball=Ball(0,0,2,3,40,"black")

num_balls=5
min_ball_r=10
max_ball_r=100
min_ball_dx=-2
max_ball_dx=2
min_ball_dy=-2
max_ball_dy=2

food=[]
for i in range(40):
	x= random.randint(-SCREEN_WIDTH + max_ball_r, SCREEN_WIDTH - max_ball_r)
	y= random.randint(-SCREEN_HEIGHT + max_ball_r, SCREEN_HEIGHT - max_ball_r)
	dx=0
	dy=0
	r= 4
	color= (random.random(), random.random(), random.random())
	food.append(Ball(x,y,dx,dy,r,color))


balls=[]
for i in range(num_balls):
	x= random.randint(-SCREEN_WIDTH + max_ball_r, SCREEN_WIDTH - max_ball_r)
	y= random.randint(-SCREEN_HEIGHT + max_ball_r, SCREEN_HEIGHT - max_ball_r)
	dx= random.randint(min_ball_dx, max_ball_dx)
	dy= random.randint(min_ball_dy, max_ball_dy)
	r= random.randint(min_ball_r, max_ball_r)
	color= (random.random(), random.random(), random.random())
	while x in range(int(my_ball.xcor()-my_ball.r), int(my_ball.xcor()+my_ball.r) ):
		x= random.randint(-SCREEN_WIDTH + max_ball_r, SCREEN_WIDTH - max_ball_r)
	while y in range(int(my_ball.ycor()-my_ball.r), int(my_ball.ycor()+my_ball.r) ):
		y= random.randint(-SCREEN_HEIGHT + max_ball_r, SCREEN_HEIGHT - max_ball_r)
	while dx==0:
		dx= random.randint(min_ball_dx, max_ball_dx)
	while dy==0:
		dy= random.randint(min_ball_dy, max_ball_dy)
	balls.append(Ball(x, y, dx, dy, r, color))

for i in balls:
	i.move(SCREEN_WIDTH, SCREEN_HEIGHT)

def collide(ball1, ball2):
	if ball1 == ball2:
		return False
	d= math.sqrt(math.pow((ball2.xcor()-ball1.xcor()),2) + math.pow((ball2.ycor()-ball1.ycor()),2))
	if d+10 <= ball1.r+ball2.r:
		return True
	else:
		return False
def all_collide():
	for ball1 in balls:
		for ball2 in balls:
			if collide(ball1, ball2)==True:
				r1=ball1.r
				r2=ball2.r
				if r1>r2:
					randomize(ball1,ball2)
				else:
					randomize(ball2,ball1)

def randomize(bigger,smaller,  isFood = False):
	x= random.randint(-SCREEN_WIDTH + max_ball_r, SCREEN_WIDTH - max_ball_r)
	y= random.randint(-SCREEN_HEIGHT + max_ball_r, SCREEN_HEIGHT - max_ball_r)
	dx=0
	dy=0
	while x in range(int(my_ball.xcor()-my_ball.r-5), int(my_ball.xcor()+my_ball.r+5) ):
		x= random.randint(-SCREEN_WIDTH + max_ball_r, SCREEN_WIDTH - max_ball_r)
	while y in range(int(my_ball.ycor()-my_ball.r-5), int(my_ball.ycor()+my_ball.r+5) ):
		y= random.randint(-SCREEN_HEIGHT + max_ball_r, SCREEN_HEIGHT - max_ball_r)
	while dx==0:
		dx= random.randint(min_ball_dx, max_ball_dx)
	while dy==0:
		dy= random.randint(min_ball_dy, max_ball_dy)
	r= random.randint(min_ball_r, max_ball_r)
	color= (random.random(), random.random(), random.random())
	if isFood:
		dx = 0
		dy = 0
		r = 4
		bigger.r += 0.5
	else:
		bigger.r=bigger.r+3
	smaller.dx=dx
	smaller.dy=dy
	smaller.r=r
	smaller.color(color)
	smaller.shape("circle")
	smaller.shapesize(r/10)
	smaller.penup()
	smaller.goto(x,y)

	
	bigger.shapesize(bigger.r/10)
def my_collide():
		for rand_ball in balls:
			if collide(my_ball, rand_ball)==True:
				my_r=my_ball.r
				r_r=rand_ball.r
				if my_r>r_r:
					randomize(my_ball,rand_ball)
				else:
					return False 
		for i in food:
			if collide(my_ball, i)==True:
				randomize(my_ball,i, True)

		return True
def movearound(event):
	my_ball.goto(event.x-SCREEN_WIDTH, SCREEN_HEIGHT-event.y)
turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()



while RUNNING==True:
	SCREEN_WIDTH = turtle.getcanvas().winfo_width()//2
	SCREEN_HEIGHT = turtle.getcanvas().winfo_height()//2
	for ball in balls:
		ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)
	if my_collide()==False:
		RUNNING=False
	all_collide()
	turtle.update()
	time.sleep(SLEEP)