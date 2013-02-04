# Quetzaloid
# Modulo de Unidades de Longitud
# 4 Enero del 2013

# clase Milimeter
# contiene :
# * la informacion de milimetros
# * las funciones necesarias para la conversion entre unidades
# * los operadores basicos +,- para operaciones entre unidades similares o diferentes
class Milimeter:
    def __init__(self,val):
        self.val = val
        self.type = 'milimeter'
    def toCentimeter(self):
        return Centimeter((self.val*1.000)/10)
    def toMeter(self):
        return self.toCentimeter().toMeter()
    def toKilometer(self):
        return self.toMeter().toKilometer()

    def __add__(self,obj):
        ret = 0
        if obj.type!=self.type:
            ret = self.val + obj.toMilimeter().val
        else :
            ret = self.val + obj.val
        return Milimeter(ret)
    def __sub__(self,obj):
        ret = 0
        if obj.type!=self.type:
            ret = self.val - obj.toMilimeter().val
        else :
            ret = self.val - obj.val
        return Milimeter(ret)

# clase Centimeter
# contiene :
# * la informacion de centimetros
# * las funciones necesarias para la conversion entre unidades
# * los operadores basicos +,- para operaciones entre unidades similares o diferentes
class Centimeter:
    def __init__(self,val):
        self.val = val
        self.type = 'centimeter'
    def toMeter(self):
        return Meter((self.val*1.000)/100)
    def toKilometer(self):
        return self.toMeter().toKilometer()
    def toMilimeter(self):
        return Milimeter(self.toMeter().toMilimeter().val)
    def __add__(self,obj):
        ret = 0
        if obj.type!=self.type:
            ret = self.val + obj.toCentimeter().val
        else :
            ret = self.val + obj.val
        return Centimeter(ret)

    def __sub__(self,obj):
        ret = 0
        if obj.type!=self.type:
            ret = self.val + obj.toCentimeter().val
        else :
            ret = self.val + obj.val
        return Centimeter(ret)

# clase Meter
# contiene :
# * la informacion de metros
# * las funciones necesarias para la conversion entre unidades
# * los operadores basicos +,- para operaciones entre unidades similares o diferentes
class Meter :
    def __init__(self,val):
        self.val = val
        self.type = 'meter'
    def toKilometer(self):
        k = Kilometer((self.val*(1.000))/1000)
        return k
    def toCentimeter(self):
        return Centimeter((self.val)*100)
    def toMilimeter(self):
        return Milimeter((self.toCentimeter().val*10))
    def toMeter(self):
        return self
	
    def __add__(self,obj):
        ret = 0
        if obj.type!=self.type:
            ret = self.val + obj.toMeter().val
        else:
            ret = self.val + obj.val
        return Meter(ret)

    def __sub__(self,obj):
        if obj.type!=self.type:
            ret = self.val - obj.toMeter().val
        else :
            ret = self.val - obj.val
        return Meter(ret)

# clase Kilometer
# contiene :
# * la informacion de kilometros
# * las funciones necesarias para la conversion entre unidades
# * los operadores basicos +,- para operaciones entre unidades similares o diferentes
class Kilometer:
    def __init__(self,val):
        self.val = val
        self.type = 'kilometer'
    def toMeter(self):
        return Meter(self.val*1000)
    def toCentimeter(self):
        return self.toMeter().toCentimeter()
    def toMilimeter(self):
        return self.toMeter().toMilimeter()
    def __add__(self,obj):
        ret = 0
        if obj.type!=self.type:
            ret = self.val + obj.toKilometer().val
        else :
            ret = self.val + obj.val
        return Kilometer(ret)

    def __sub__(self,obj):
        ret = 0
        if obj.type!=self.type:
            ret = self.val + obj.toKilometer().val
        else :
            ret = self.val + obj.val
        return Kilometer(ret)
