# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
import random


class Floater(Prey):
    radius= 5
    def __init__(self,x,y):
        Prey.__init__(self,x,y,10,10,0,5)
        self.randomize_angle()
        self._image = PhotoImage(file='ufo.gif') 
    def update(self, model):
        y = random.randint(0,100)
        if y <= 30:
            x = random.uniform(-.5,.5)
            z = random.uniform(-.5,.5)
            if self._speed + x > 7:
                self._speed == 7
            elif self._speed + x < 3:
                self._speed == 3
            else:
                self._speed += x
            self._angle += (z)     
        self.move()
    def display(self,the_canvas):
        the_canvas.create_image(*self.get_location(),image=self._image)
