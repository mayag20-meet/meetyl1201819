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
	

