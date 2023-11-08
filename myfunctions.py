import stdio

def max3(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
        
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
    
def majority(a, b, c):
    return (a and b) or (a and c) or (b and c)

def add3(a, b, c):
    return a + b + c

#test client
def main():
    a = 4
    b = 5
    c = 5.5
    stdio.writeln(max3(a, b, c))
    a = True
    b = False
    c = True
    stdio.writeln(isodd(a, b, c))
    a = True
    b = False
    c = True
    stdio.writeln(majority(a, b, c))
    a = 1
    b = 2
    c = 3
    stdio.writeln(add3(a, b, c))
    


if __name__ == '__main__':
    main()
    