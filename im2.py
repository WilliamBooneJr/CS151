#Billy Boone
#This program takes the name of a picture file as a command-line argument and flips the image horizontally. 

import sys
import stdio
import stddraw
from picture import Picture

# Accept the name of a JPG or PNG file as a command-line argument.


pic = Picture(sys.argv[1])

width = pic.width()
height = pic.height()

# Create a new image with swapped width and height.
rotated_pic = Picture(height, width)

for col in range(width):
    for row in range(height):
        pixel = pic.get(col, row)
        # Copy the pixel to the rotated image with switched coordinates.
        rotated_pic.set(row, width - col - 1, pixel)

stddraw.setCanvasSize(height, width)
stddraw.picture(rotated_pic)
stddraw.show()
        