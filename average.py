import stdio

total = 0.0
count = 0
nums = []

while not stdio.isEmpty():
    value = stdio.readFloat()
    nums += [value]
maximum = int(max(nums))
minimum = int(min(nums))

stdio.writeln('Max is ' + str(maximum))
stdio.writeln('Min is ' + str(minimum))