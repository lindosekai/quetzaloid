# Quetzaloid Velocity

class Velocity:
    def __init__(self,dist,time):
        self.dist = dist
        self.time = time
        self.__name__ = 'vel'
        self.val = (self.dist.val*(1.000))/(self.time.val*(1.000))
    def type(self):
        return self.dist.type,self.time.type
    def convertTo(self,str):
        pats = str.split('/')
        if pats[0] == 'm':
            self.dist = self.dist.toMeter()
        elif pats[0] == 'km':
            self.dist = self.dist.toKilometer()
        
        if pats[1]=='s':
            self.time = self.time.toSecond()
        elif pats[1]=='h':
            self.time = self.time.toHour()
        self.val = (self.dist.val*(1.000))/(self.time.val*(1.000))
