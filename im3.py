#Billy Boone
#This program takes the name of a picture file as a command-line input, and creates three images:
#one with only the red components, one with only the green components,and one with only the blue components

import sys
import stddraw
from picture import Picture
from color import Color  # Import the Color class

# Accept the name of a JPG or PNG file as a command-line argument.
pic = Picture(sys.argv[1])

width = pic.width()
height = pic.height()

# Create new images for red, green, and blue components
red_pic = Picture(width, height)
green_pic = Picture(width, height)
blue_pic = Picture(width, height)

for col in range(width):
    for row in range(height):
        # Get the pixel at the current column and row
        pixel = pic.get(col, row)

        # Extract the red, green, and blue components
        red = pixel.getRed()
        green = pixel.getGreen()
        blue = pixel.getBlue()

        # Create Color objects for each component
        red_color = Color(red, 0, 0)
        green_color = Color(0, green, 0)
        blue_color = Color(0, 0, blue)

        # Set the corresponding color in the new images
        red_pic.set(col, row, red_color)
        green_pic.set(col, row, green_color)
        blue_pic.set(col, row, blue_color)


stddraw.setCanvasSize(width * 3, height)
stddraw.setXscale(0, width * 3)
stddraw.setYscale(0, height)


# Display the red image
stddraw.picture(red_pic, width * 0.5)

# Display the green image
stddraw.picture(green_pic, width * 1.5)

# Display the blue image
stddraw.picture(blue_pic, width * 2.5)

stddraw.show()



