#Compose a function histogram() that takes an array a[] of integers and an integer m as arguments 
#and returns an array of length m whose ith element is the number of times the integer i appears 
#in the argument array.  Assume that the values in a[] are all between 0 and m-1, 
#so that the sum of values in the returned array should be equal to len(a).

import stdarray
import stdio
import sys

array = stdio.readAllInts()
m = int(sys.argv[1])

def histogram(a, m):
    #create an array of length m
    b = stdarray.create1D(m, 0)
    #for each element in a, add 1 to the corresponding element in b
    for i in range(len(a)):
        b[a[i]] += 1
    return b

def main():
    stdio.writeln(array)
    stdio.writeln(histogram(array, m))

if __name__ == '__main__':
    main()

