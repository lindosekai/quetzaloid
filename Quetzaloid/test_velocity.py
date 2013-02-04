#Quetzaloid Velocity test
# 4 Enero 2013

from Quetzaloid.Velocity import *
from Quetzaloid.Longitud import *
from Quetzaloid.Time import *

v = Velocity(Kilometer(100),Minute(60))
print "{0}/{1} = {2}".format(v.type()[0],v.type()[1],v.val)

print v.dist.val
print v.time.val
print v.val

v2 = Velocity(Meter(1),Second(1))
print v2.val
print v2.type()
v2.convertTo('m/h')
print v2.val
print v2.type()