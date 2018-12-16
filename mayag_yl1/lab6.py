import turtle
from turtle import Turtle
import random
turtle.colormode(255)

"""1
class Square(Turtle):
	def __init__(self, size):
		Turtle.__init__(self)
		self.shape("square")
		self.shapesize(size)
	def rand_color(self):
		r=random.randint(0,256)
		b=random.randint(0,256)
		g=random.randint(0,256)
		self.color(r,b,g)

x=Square(9)
x.rand_color()"""

turtle.register_shape("hax", ((0.00,0.00), (100.00,0.00), (128.19,10.26), (136.87,59.50), (154.24,157.98), (149.03,187.53), (102.04,204.63)))

class Haxagon(Turtle):
	def __init__(self, size):
		Turtle.__init__(self)
		self.shape("hax")
		self.shapesize(size)

x = Haxagon(2)

turtle.begin_poly()
for i in range(6):
	turtle.fd(50)
	turtle.left(60)
turtle.end_poly()
p = turtle.get_poly()
print(p)
#register_shape("myFavouriteShape", p)



turtle.mainloop()