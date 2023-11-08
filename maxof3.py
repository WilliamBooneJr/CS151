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
        
def main():
    a = float(stdio.readString())
    b = float(stdio.readString())
    c = float(stdio.readString())
    stdio.writeln(max3(a, b, c))

if __name__ == '__main__':
    main()
    