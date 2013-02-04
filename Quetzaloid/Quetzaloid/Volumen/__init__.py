# Quetzaloid Volumen

class Cube:
    def __init__(self,long):
        self.long = long
        self.val = self.value()
    def value(self):
        return self.long.val*self.long.val*self.long.val