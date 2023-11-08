#Billy Boone
#this program draws the sierpinski triangle pattern similar to htree but with triangles
#n is passed in as the level of recursion depth.

import sys
import stddraw
import stdrandom

n = int(sys.argv[1])

x1 = 0.0 #vertices of the outer triangle
y1 = 0.0
x2 = 1.0
y2 = 0.0
x3 = 0.5
y3 = 0.866


stddraw.setPenRadius(0.0)

def draw_triangles(n, x1, y1, x2, y2, x3, y3):
    if n == 0: #base case
        return
    else:
        # Draw the outer triangle
        stddraw.line(x1, y1, x2, y2)
        stddraw.line(x1, y1, x3, y3)
        stddraw.line(x2, y2, x3, y3)

        # Calculate midpoints of the edges
        mx1 = (x1 + x2) / 2
        my1 = (y1 + y2) / 2
        mx2 = (x2 + x3) / 2
        my2 = (y2 + y3) / 2
        mx3 = (x1 + x3) / 2
        my3 = (y1 + y3) / 2

        # Draw the inner triangles 
        draw_triangles(n - 1, x1, y1, mx1, my1, mx3, my3) #The first call is for the triangle defined by vertices 1, midpoint 1, and midpoint 3.
        draw_triangles(n - 1, x2, y2, mx1, my1, mx2, my2) #The second call is for the triangle defined by vertices 2, midpoint 1, and midpoint 2.
        draw_triangles(n - 1, x3, y3, mx2, my2, mx3, my3) #The third call is for the triangle defined by vertices 3, midpoint 2, and midpoint 3.
       
        

draw_triangles(n, x1, y1, x2, y2, x3, y3)
stddraw.show()

