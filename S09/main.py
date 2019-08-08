import sys
import pprint

pprint.pprint(sys.path)
import geom

r = geom.Rectangle(2.0, 5.0)
print(r.area)