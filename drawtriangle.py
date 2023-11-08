import stddraw
import math

stddraw.setXscale(0, 3.0)
stddraw.setYscale(0, 3.0)
t = math.sqrt(3.0) / 2.0
stddraw.line(0.0, 0.0, 1.0, 0.0)    
stddraw.line(1.0, 0.0, 0.5, t)
stddraw.line(0.5, t, 0.0, 0.0)
stddraw.point(0.5, t/3.0)

#draw a square
#set color
stddraw.setPenColor(stddraw.LIGHT_GRAY)
stddraw.filledSquare(1.5, 1.5, 0.25)
stddraw.show()