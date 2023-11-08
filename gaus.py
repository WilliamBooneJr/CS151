#Billy Boone
#10/9/2023
#This program will experiment with the following function for generating random variables 
#from the Gaussian distribution (which is based on generating a random point in the unit circle 
#and using a form of the Box-Muller transform).
"""def gaussian():
    r = 0.0
    while (r >= 1.0) or (r == 0.0):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        r = x*x + y*y
    return x * math.sqrt(-2.0 * math.log(r) / r)

Take a command-line argument n and generate n random numbers, using an array a[] of 20 integers to count the 
numbers generated that fall between i*.05 and (i+1)*.05 for i from 0 to 19. 
Then use stddraw to plot the values and to compare your result with the normal bell curve. """

import random
import math
import stdio
import stddraw
import sys
import stdarray

n = int(sys.argv[1]) #get input and initialize array
a = stdarray.create1D(20, 0)

#defining the gaussian function
def gaussian():
    r = 0.0
    while (r >= 1.0) or (r == 0.0):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        r = x*x + y*y
    return x * math.sqrt(-2.0 * math.log(r) / r)

#generate n random gaussian values and record them in the array a
for i in range(n):
    x = gaussian()
    if (x >= 0.0) and (x <= 1.0):
        a[int(x*20)] += 1

#plot the frequencies in the array a in a histogram
stdio.writeln(a)
stddraw.setYscale(0, max(a) + 10) #scale the window
stddraw.setXscale(0, 21)
stddraw.setPenRadius(0.0)
for i in range(20):
    stddraw.filledRectangle(i, 0, 0.5, a[i]) #draw each bar at (i(1-19), 0) with width 0.5 and height a[i]
stddraw.show()




