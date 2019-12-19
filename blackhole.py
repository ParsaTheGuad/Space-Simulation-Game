# Black_Hole is singly derived from Simulton, updating by finding+removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius= 10
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,2*Black_Hole.radius,2*Black_Hole.radius)
    def update(self, model):
        Preyset = model.find(lambda x: isinstance(x, Prey))
        nset = set()
        for i in Preyset:
            if self.contains(i.get_location()):
                nset.add(i)
        return nset
    def display(self, canvas):
        canvas.create_oval(self.get_location()[0]-(self.get_dimension()[0]/2), self.get_location()[1]-(self.get_dimension()[0]/2),self.get_location()[0]+(self.get_dimension()[0]/2), self.get_location()[1]+(self.get_dimension()[0]/2), fill='black')
    def contains(self, other):
        return self.get_dimension()[0]/2 > self.distance(other)