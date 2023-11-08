import stdio
import sys

n = stdio.readInt()

def countdown(n):
    if n == 0:
        stdio.writeln("down!")
    else:
        stdio.writeln(n)
        return countdown(n-1)

countdown(n)