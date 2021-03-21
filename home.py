import graphics.rectangle
from graphics.dgraphics import sphere
print("area of rectangle:",graphics.rectangle.area(3,4))
print("perimeter of rectangle:",graphics.rectangle.perimeter(3,4))

from graphics.circle import *
print("area of circle:",area(2))
print("perimeter of circle",perimeter(2))

from graphics.dgraphics.cuboid import area
print("area of cuboid:",area(1,2,3))

from graphics.dgraphics.cuboid import perimeter
print("perimeter of cuboid:",perimeter(1,2,3))

import graphics.dgraphics.sphere
print("area of sphere:",graphics.dgraphics.sphere.area(2))
print("perimeter of sphere:",graphics.dgraphics.sphere.perimeter(2))