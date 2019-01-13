import turtle
import time
import random
from ball.py import Ball

turtle.tracer(0,0)
turtle.hideturtle()
boolean RUNNING set to True
float SLEEP set to 0.0077
SCREEN_WIDTH set to turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT set to turtle.getcanvas().winfo_height()/2

my_ball=Ball(0,0,2,3,25,"blue")

num_balls=5
min_ball_r=10
max_ball_r=100
min_ball_dx=-5
max_ball_dx=5
min_ball_dy=-5
max_ball_dy=5

balls=[]
for i in range(num_balls):
	x= random.randint(-SCREEN_WIDTH + max_ball_r, SCREEN_WIDTH - max_ball_r)
	y= random.randint(-SCREEN_HEIGHT + max_ball_r, SCREEN_HEIGHT - max_ball_r)
	dx= random.randint(min_ball_dx, max_ball_dx)
	dy= random.randint(min_ball_dy, max_ball_dy)
	r= random.randint(min_ball_r, max_ball_r)
	color= (random.random(), random.random(), random.random())
	balls.append(Ball(x, y, dx, dy, r, color))

for i in (balls[]):
	i.move(SCREEN_WIDTH, SCREEN_HEIGHT)

def collide(Ball1, Ball2):
	if ball1 == ball2:
		return False
	d= math.sqrt(math.pow((Ball2.x-Ball1.x),2) + math.pow((Ball2.y-Ball1.y),2))
	if d+10 <= Ball1.r+Ball2.r:
		return True
	else:
		return False
def all_collide():
	for Ball1, ball2 in (balls[]):




