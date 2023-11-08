#Compose a function rescale() that takes an array a[] of strictly positive floats
# as its argument and rescales the array so that each element is between 0 and 1 
#(by subtracting the minimum value from each element and then dividing each element by 
#the difference between the minimum and maximum values).  Use the built-in max() and min() functions. 

import stdarray
import stdio
import sys

array = stdio.readAllFloats()


def rescale(a):
    #find the min and max values in the array
    minimum_value = min(a)
    maximum_value = max(a)
    difference_value = maximum_value - minimum_value
    #subtract the min value from each element and divide by the difference between the min and max values
    for i in range(len(a)):
        a[i] -= minimum_value
        a[i] /= difference_value

    return a

def main():
    rescale(array)
    stdio.writeln(array)

if __name__ == '__main__':
    main()