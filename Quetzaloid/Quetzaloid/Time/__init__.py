# Quetzaloid Time

class Second:
    def __init__(self,val):
        self.val = val
        self.type = 'second'
    def toMinute(self):
        return Minute((self.val*1.000)/60)
    def toHour(self):
        return Hour(self.toMinute().toHour().val)
    def toSecond(self):
        return self

class Minute:
    def __init__(self,val):
        self.val = val
        self.type = 'minute'
    def toSecond(self):
        return Second(self.val*60)
    def toHour(self):
        return Hour((self.val*1.000)/60)
    def toMinute(self):
        return self

class Hour:
    def __init__(self,val):
        self.val = val
        self.type = 'hour'
    def toMinute(self):
        return Minute(self.val*60)
    def toSecond(self):
        return Second(self.toMinute().val*60)
    def toHour(self):
        return self