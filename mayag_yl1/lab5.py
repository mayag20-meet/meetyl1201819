"""1
import tkinter as tk
from tkinter import simpledialog

#Then when ever you want to ask the user for input use this code
greeting = simpledialog.askstring("Input", "Hello, possible pirate! What's the password?", parent=tk.Tk().withdraw())
if greeting in ["Arrr!"]:
	print("Go away, pirate.")
else:
	print("Greetings, hater of pirates!")"""


"""2
import tkinter as tk
from tkinter import simpledialog
# A time traveler has suddenly appeared in your classroom!
# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).
year = int(simpledialog.askstring("Input", "Greetings! What is your year of origin?", parent=tk.Tk().withdraw()))
if year <= 1900:
    print ("Woah, that's the past!")
elif year > 1900 & year < 2020:
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")"""


# Write a simple class that defines a person
# with attributes of first_name, last_name
# and has a method signature of "speak" which
# prints the object as "Jefferson, Thomas".

class Person:
  def __initalize__(self, first_name, last_name):
    self.first = first_name
    self.last = last_name
  def speak(self):
  	print("Jefferson, Thomas")

me = Person("Brandon", "Walsh")
you = Person("Ethan", "Reed")

me.speak()
you.speak()

