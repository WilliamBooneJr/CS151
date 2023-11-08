import random
import stdio

my_list = []


for i in range(5):
    num = random.random()
    stdio.writeln(num)
    my_list.append(num)
    

avg = sum(my_list) / 5
largest = max(my_list)
smallest = min(my_list)

stdio.writeln("Average: " + str(avg))
stdio.writeln("Max: " + str(largest))
stdio.writeln("Minimum: " + str(smallest))

