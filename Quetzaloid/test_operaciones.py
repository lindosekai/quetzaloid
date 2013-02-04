# Quetzaloid framework
# 4 Enero del 2013
# Conversiones matematicas
# Prueba de operaciones Aritmeticas entre Diferentes Tipos
# Milimetro, Centimetro, Metro, Kilometro

from Quetzaloid.Longitud import *

m1 = Meter(20.5)
m2 = Meter(14.7)
c1 = Centimeter(2535)
m3 = m1 + m2
m4 = m1 + c1
m5 = m1 - m2
print "c1 - {0} - {1}".format(c1.type,c1.val)
print "m1 - {0} - {1}".format(m1.type,m1.val)
print "m2 - {0} - {1}".format(m2.type,m2.val)
print "m3 - {0} - {1} (m1+m2)".format(m3.type,m3.val)
print "m4 - {0} - {1} (m1+c1)".format(m4.type,m4.val)
print "m5 - {0} - {1} (m1-m2)".format(m5.type,m5.val)

mil1 = Milimeter(10)
mil2 = Milimeter(20)
cen1 = Centimeter(1)
kil1 = Kilometer(1)
print (mil1+cen1).val
print (mil2-mil1).val
print "{0} - {1}".format((kil1+mil1).val,(kil1+mil1).type)
print "{0} - {1}".format((mil1+kil1).val,(mil1+kil1).type)