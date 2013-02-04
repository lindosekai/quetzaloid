# Quetzaloid framework
# 4 Enero del 2013
# Conversiones matematicas
# Prueba basica de Conversiones entre metro y Sus Derivados
# Milimetro, Centimetro, Metro, Kilometro
from Quetzaloid import Meter
from Quetzaloid import Kilometer

m = Meter(1)
c = m.toCentimeter()
mil = m.toMilimeter()
print "+++  Quetzaloid Framework +++"
print "+++   4 Enero del 2013    +++"
print 
print "en {0} metros hay ...".format(m.val)
print "{0} Centimetros".format(m.toCentimeter().val)
print "{0} Milimetros".format(m.toMilimeter().val)
print "{0} Kilometros".format(m.toKilometer().val)
print
print "en {0} centimetros hay ...".format(c.val)
print "{0} milimetros".format(c.toMilimeter().val)
print "{0} Metros".format(c.toMeter().val)
print "{0} Kilometros".format(c.toKilometer().val)
print 
print "en {0} Milimetros hay ...".format(mil.val)
print "{0} Centimetros".format(mil.toCentimeter().val)
print "{0} Metros".format(mil.toMeter().val)
print "{0} Kilometros".format(mil.toKilometer().val)