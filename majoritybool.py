import stdio

#return true if the majority of a, b, c are true
#cannnot use an if statement

def majority(a, b, c):
    return (a and b) or (a and c) or (b and c)

a = stdio.readBool()
b = stdio.readBool()
c = stdio.readBool()
stdio.writeln(majority(a, b, c))

    