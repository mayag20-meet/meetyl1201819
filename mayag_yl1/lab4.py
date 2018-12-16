
class animal(object):
	def __init__(self,sound,name,age,fave_color):
		self.sound=sound
		self.name=name
		self.age=age
		self.fave_color=fave_color
	def eat(self,food):
		print("yummy!! "+self.name+ " is eating "+food)
	def description(self):
		print(self.name +" is "+str(self.age)+" years old and loves the color "+self.fave_color)
	def make_sound(self,times):
		print(self.sound*times)


#a=animal("bark","max",5,"blue")
#a.eat("meat")
#a.description()
#a.make_sound(2)

class person(object):
	def __init__(self, name, gender, age, city, hobby):
		self.name=name
		self.gender=gender
		self.age=age
		self.city=city
		self.hobby=hobby
	def eat_morning(self,breakfast):
		print(self.name+" is eating her favorite breakfast- "+breakfast)

#a=person("maya", "female", 15, "jerusalem", "sports")
#a.eat_morning("cornflakes")

class song(object):
	def__init__(self, lyrics):
		self.lyrics=(lyrics)
	def sing_a_song(self, ):
		print


