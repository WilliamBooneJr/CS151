import stdio
import stddraw

#pass input of number of circles and recursively draw n circles
stddraw.setXscale(-1, 1)
stddraw.setYscale(-1, 1)

n = 50
x = 0
y = 0
r = 1

def drawcircle(n, x, y, r):
    if n == 0:
        return "no circles"
    else:
        stddraw.circle(x,y,r)
        return drawcircle(n-1, x, y, r - .02)
    
drawcircle(n, x, y, r)
stddraw.show()  