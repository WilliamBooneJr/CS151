#Billy Boone
#Compose a program that takes the name of a picture file as a command-line argument and flips the image horizontally. 

import sys
import stdio
import stddraw
from picture import Picture

# Accept the name of a JPG or PNG file as a command-line argument.


pic = Picture(sys.argv[1])

width = pic.width()
height = pic.height()

for col in range(width): #loop through the picture pixel columns
    for row in range(height): #loop through the picture pixel rows
        pixel = pic.get(col, row) #get the pixel at the current column and row
        pic.set(width - col - 1, row, pixel)

stddraw.setCanvasSize(width, height)
stddraw.picture(pic)
stddraw.show()

        
