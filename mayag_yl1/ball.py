from turtle import *
import turtle

class Ball(Turtle):
	def __init__(self, x, y, dx, dy, r, color):
		Turtle.__init__(self)
		self.x=x
		self.y=y
		self.dx=dx
		self.dy=dy
		self.r=r
		self.color(color)
		self.shape("circle")
		self.shapesize(r/10)
		self.penup()
		self.goto(x,y)
	def move(self, screen_width, screen_height):
		current_x, current_y= self.pos()
		new_x= current_x+self.dx
		new_y= current_y+self.dy
		right_side_ball=new_x+self.r
		left_side_ball=new_x-self.r
		top_side_ball=new_y+self.r
		bottom_side_ball=new_y-self.r
		self.goto(new_x, new_y)
		if right_side_ball>screen_width:
			self.dx= -self.dx
		if left_side_ball<-screen_width:
			self.dx= -self.dx
		if top_side_ball>screen_height:
			self.dy= -self.dy
		if bottom_side_ball<-screen_height:
			self.dy= -self.dy

"""a=Ball(30, 30, 2, 3, 10, "blue")
while True:
	a.move(200, 200)"""







