import stdio
import sys

n = int(sys.argv[1])
total = 0   
for i in range(n):
    total += stdio.readInt() #Standard input reads in a constant flow of input
stdio.writeln('Sum is ' + str(total))

