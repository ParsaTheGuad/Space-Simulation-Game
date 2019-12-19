# Hunter is doubly-derived from the Mobile_Simulton and Pulsator classes:
#   updating/displaying like its Pulsator base, but also moving (either in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.
from tkinter import *
from PIL import Image, ImageTk
from hunter import Hunter

#This Special simulton is a hunter with a starting speed of 10 and that speeds up every time it eats a prey by 5
#and slows down after not eating for 20 cycles, once it is in starvation mode it loses one speed per cycle until 
#it either eats or has no speed and dies.

class Special(Hunter):
    def __init__(self,x,y):
        Hunter.__init__(self, x, y)
        self._counter1 = 0
        self._speed = 10
        img = Image.open("sonic.gif")
        self._img = img.resize((20,20))
        self._image =  ImageTk.PhotoImage(self._img)
    def update(self, model):
        self._counter = 0
        self._counter1 += 1
        x = Hunter.update(self,model)
        if len(x) != 0:
            self._speed += 5
            self._counter1 = 0
        if self._counter1 > 20:
            self._speed -= 1
        if self._speed == 0:
            x.add(self)    
        return x
    def display(self,the_canvas):
        the_canvas.create_image(*self.get_location(),image=self._image)