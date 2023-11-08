#Billy Boone
#10/4/2023

#This program takes a 5 or 9 digit zipcode and converts it to a barcode
#Functions are implemented for each step

import stddraw
import stdio
import sys

#Constant for bar spacing
BAR_SPACING = 0.02


# Attach the sequence of bars for each digit to a key
key = {
    '1': [0.5, 0.5, 0.5, 1.0, 1.0],
    '2': [0.5, 0.5, 1.0, 0.5, 1.0],
    '3': [0.5, 0.5, 1.0, 1.0, 0.5],
    '4': [0.5, 1.0, 0.5, 0.5, 1.0],
    '5': [0.5, 1.0, 0.5, 1.0, 0.5],
    '6': [0.5, 1.0, 1.0, 0.5, 0.5],
    '7': [1.0, 0.5, 0.5, 0.5, 1.0],
    '8': [1.0, 0.5, 0.5, 1.0, 0.5],
    '9': [1.0, 0.5, 1.0, 0.5, 0.5],
    '0': [1.0, 1.0, 0.5, 0.5, 0.5]
}

# Function to draw a half-height or full-height bar
def draw_bar(size, x_position):
    if size == 1:
        stddraw.line(x_position, 0.4, x_position, 0.8)  # Draw a full-height bar
    else:
        stddraw.line(x_position, 0.4, x_position, 0.6)  # Draw a half-height bar

# Function to translate a digit to its sequence of bars
def translate_digit(digit):
    global x_position #keep track of x_position
    values = key.get(str(digit)) #Get sequence of values from corresponding key and assign them to variable to iterate through
    for size in values:
        draw_bar(size, x_position)
        x_position += BAR_SPACING #increment x_position


# Function to compute the checksum digit
def compute_checksum(zipcode):
    total = sum(int(digit) for digit in zipcode)
    checksum = total % 10
    return str(checksum)

# Get the ZIP code from command-line argument
zipcode = sys.argv[1]

# Set up the drawing scale
stddraw.setXscale(0, len(zipcode) * 0.131) #scale the x axis based upon fractional length of zipcode
stddraw.setYscale(0, 1)

# Initialize the starting position for drawing
x_position = 0.02

# Draw the guard rail (full-height bar) at the beginning
draw_bar(1, x_position)
x_position += BAR_SPACING

# Draw the bars for each digit in the ZIP code
for digit in zipcode:
    translate_digit(digit)

# Compute and draw the checksum digit
checksum_digit = compute_checksum(zipcode)
translate_digit(checksum_digit)

# Draw the guard rail (full-height bar) at the end
draw_bar(1, x_position)

# Display the barcode
stddraw.show()