from turtle import *
import turtle
import random
import math

class Ball(Turtle):
	def __init__(self,radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius=radius
		self.color(color)
		self.speed(speed)

ball1=Ball(100, "red", 10)
ball2=Ball(50, "blue", 10)
ball3=Ball(10, "yellow", 10)

def check_collision(ball1, ball2):
	x1 = ball1.xcor()
	y1 = ball1.ycor()
	x2 = ball2.xcor()
	y2 = ball2.ycor()
	r1 = ball1.radius
	r2 = ball2.radius
	d = math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))
	

	if ((r1+r2)<d):
		"""for 2
		print("no collision")
	else:
		ball2.color("green")
check_collision(ball1, ball2)"""
	

	#for 3
		return False
	else:
		return True


ball_list = [ball1, ball2, ball3,]	
def check_list(ball_list):
	for a in ball_list:
		for b in ball_list:
			if a != b:
				if check_collision(a, b): 
					a.goto(0,0)
					b.goto(100,0)






turtle.mainloop()

