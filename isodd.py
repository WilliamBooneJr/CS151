import stdio

def isodd(a, b, c):
    count = 0
    if a == True:
        count += 1
    if b == True:
        count += 1
    if c == True:
        count += 1
    if count == 1 or count == 3:
        return True
    else:
        return False

 
    


a = (stdio.readBool())
b = (stdio.readBool())
c = (stdio.readBool())
stdio.writeln(isodd(a, b, c))





