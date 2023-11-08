import stdio
import sys
import stddraw

# Accept integer n as a command-line argument. Draw an n-by-n checkerboard

n = int(sys.argv[1])
stddraw.setXscale(0, n)
stddraw.setYscale(0, n)

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            stddraw.setPenColor(stddraw.DARK_GRAY)
        else:
            stddraw.setPenColor(stddraw.LIGHT_GRAY)
        stddraw.filledSquare(i + 0.5, j + 0.5, 0.5)

stddraw.show()
