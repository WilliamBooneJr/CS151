#Create a class called Point. Point(x, y) should create a new point at coordinates (x, y).
# The distance method should return the distance between the current point and a given point passed as a parameter.

import math
import random
import stdio

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def distanceto(self, x, y):
        return math.sqrt((x - self._x)**2 + (y - self._y)**2)
    
    def __str__(self):
        return '(' + str(self._x) + ', ' + str(self._y) + ')'
    
#test client
def main():
    p = Point(1, 2)
    x = 4
    y = 6
    dist = p.distanceto(x, y)
    stdio.writeln(dist)
    stdio.writeln(p.__str__())

if __name__ == '__main__':
    main()

    
