#Billy Boone
#09/06/23
#This program calculates wind chill


#import modules
import sys
import stdio
import math

#assign variables with command-line values
temp = float(sys.argv[1])
windspeed = float(sys.argv[2])

#calculate wind chill
windchill = 35.74 + 0.6215 * (temp) + (0.4275 * (temp) - 35.75) * (windspeed ** 0.16)

#output values
stdio.write("Temperature: ")
stdio.writeln(temp)
stdio.write("Wind speed: ")
stdio.writeln(windspeed)
stdio.write("Wind chill: ")
stdio.writeln(windchill)

