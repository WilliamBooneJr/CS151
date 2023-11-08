# write the first "n" power of 2

import stdio
import sys

n = int(sys.argv[1])

for i in range(n):
    stdio.writeln(2**i)