import stdio

"""#Solve fibonacci sequence using recursion

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        stdio.writeln("fib(" + str(n-2) + ") + fib(" + str(n-1) + ")")
        return (fib(n-2) + fib(n-1))
    
stdio.writeln(fib(10))   """

import stdio

def Q2(n):
   if (n <= 0):
      return 1
   return 1 + Q2(n-2) + Q2(n-3)

stdio.writeln(Q2(4))
