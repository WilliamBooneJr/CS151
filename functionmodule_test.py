#This is the client for functinmodule.py to test the functions in functionmodule.py

import functionmodule
import sys
import stdio
import stdarray
import stdrandom 

n = int(sys.argv[1])

a = stdarray.create1D(n, 0.0)

for i in range(n):
    a[i] = stdrandom.gaussian()

stdio.writeln('stddev  = ' + str(functionmodule.calculate_std_dev(a)))
stdio.writeln('average = ' + str(functionmodule.calculate_avg(a)))



