# Hunter is doubly-derived from the Mobile_Simulton and Pulsator classes:
#   updating/displaying like its Pulsator base, but also moving (either in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):
    def __init__(self,x,y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, 2*self.radius,2*self.radius, 0, 5)
        self.randomize_angle()
    def update(self, model):
        x = Pulsator.update(self, model)
        self.move()
        Preyset = model.find(lambda x: isinstance(x, Prey))
        nset = set()
        for i in Preyset:
            if self.distance(i.get_location()) < 200:
                nset.add(i)
        closest = None
        for i in nset:
            if closest == None or self.distance(i.get_location()) < self.distance(closest.get_location()):
                closest = i
        if closest != None:
            self._angle = atan2(closest.get_location()[1]-self.get_location()[1], closest.get_location()[0]-self.get_location()[0])
        return x