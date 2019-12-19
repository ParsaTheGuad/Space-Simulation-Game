# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).


from prey import Prey
from random import random
from math import pi

class Ball(Prey): 
    radius= 5
    
    def __init__(self,x,y):
        Prey.__init__(self,x,y,10,10,0,5)
        self.randomize_angle()
    def update(self, model):
        self.move()
    def display(self, canvas):
        canvas.create_oval(self._x-5, self._y-5,self._x+5, self._y+5, fill='blue')