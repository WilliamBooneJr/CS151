#Billy Boone
#09/27/2023
#This program takes input integer n(the number of points) and float p(the probability of a point being connected to another point)
#and draws an equally spaced circle with n points and p probability of being connected to another point.

import stdio
import sys
import stddraw
import stdarray
import random
import math

# Accept integer n and float p as command-line arguments. Draw n points. 
# For each point, with probability p, draw a gray line

n = int(sys.argv[1])
p = float(sys.argv[2])

stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)

# Draw the circle of n equally spaced points on the circumference of a
# circle of radius 1, centered at (0, 0).

points = stdarray.create1D(2 * n, 0.0)  # store x and y coordinates of points
angle_increment = 2.0 * math.pi / n #compute complete circle of radians and divide by n points to evenly space points
current_angle = 0.0 #increment this to move to the next point

for i in range(0, 2 * n, 2): #Iterate through the points array and store the x and y coordinates of each point
    x = math.cos(current_angle) #compute the x coordinate based on the current angle
    y = math.sin(current_angle) #compute the y coordinate based on the current angle
    points[i] = x #store the x coordinate
    points[i + 1] = y #store the y coordinate
    current_angle += angle_increment #increment the current angle to move to the next point

for i in range(0, 2 * n, 2): 
    stddraw.point(points[i], points[i + 1]) #iterate through each pair and plot the point

# Draw gray lines between each pair of points, with probability p.

for i in range(0, 2 * n, 2): #iterate through each pair of points
    for j in range(i + 2, 2 * n, 2): #connect points without repeating
        if random.random() < p: #if the random number is less than p, draw a line between the two points
            stddraw.line(points[i], points[i + 1], points[j], points[j + 1])

stddraw.show()