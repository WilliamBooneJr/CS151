import stdio
import sys
from color import Color
import stddraw

# Accept integers r, g, and b as command-line arguments. Create instance and fill rectange with that color.
r = int(sys.argv[1])
g = int(sys.argv[2])
b = int(sys.argv[3])

# Create a Color object with the given RGB values.
color = Color(r, g, b)

# Fill a rectangle of the given color.

stddraw.setPenColor(color)
stddraw.filledRectangle(.2, .2, .2, .2)
stddraw.show()