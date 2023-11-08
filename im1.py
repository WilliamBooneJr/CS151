#Billy Boone

#Compose a program that takes the name of a grayscale picture file as a command-line argument
# and uses stddraw to plot a histogram of the frequency of occurrence of each of the 256 grayscale intensities.

import sys
import stdio
import stddraw
import luminance
import stdarray
import stdrandom
from picture import Picture

#-----------------------------------------------------------------------

# Accept the name of a JPG or PNG file as a command-line argument.
# Read an image from the file with that name. Convert to grayscale and create and show
# a histogram of the grayscale values.

values = stdarray.create1D(256, 0) #create container to store the luminance frequencies


pic = Picture(sys.argv[1]) #read in the picture object

for col in range(pic.width()): #loop through the picture pixel columns
    for row in range(pic.height()): #loop through the picture pixel rows
        pixel = pic.get(col, row) #get the pixel at the current column and row
        gray = int(luminance.luminance(pixel)) #get the luminance of the pixel
        values[gray] += 1 #increment the frequency of the luminance value

height = max(values) + 100 #draw histogram
stddraw.setCanvasSize(height, 256)
stddraw.setYscale(0, height)
stddraw.setXscale(0, 256)
for i in range(256):
    stddraw.filledRectangle(i, 0, .5, values[i])
stddraw.show()






