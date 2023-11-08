#Billy Boone
#09/06/23
#This program calculates continuously compounded interest-
#-using A = pe^rt formula


#import modules
import sys
import stdio
import math

#assign components of expression
time = float(sys.argv[1])
principal = float(sys.argv[2])
rate = float(sys.argv[3])

#calculate, round, and output
amount = principal * math.exp(rate * time)
amount = round(amount, 2)
stdio.write(amount)