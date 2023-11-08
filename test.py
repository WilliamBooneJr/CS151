import stdio
import math
import sys

n = int(sys.argv[1])

values = []

for i in range(n-1):
    values.append(stdio.readInt())

maximum = max(values)

total = 0
for i in range(maximum + 1):
    total += i

missingnum = total - sum(values)

stdio.writeln(missingnum)
#testing for github


