#Billy Boone
#09/22/2023
#This program finds the longest run of consecutive numbers in a list of numbers

import stdio

current_run = 1
longest_run = 1
nums = []
number = 0

while not stdio.isEmpty():
    value = stdio.readFloat()
    nums += [value] #add values entered to list





for i in range(len(nums)):
    if nums[i] == nums[i - 1]: #if the current number is the same as the previous number
        current_run += 1 #increment current run
        if current_run > longest_run: #if current run is greater than longest run
            longest_run = current_run
            number = nums[i]
    else:
        current_run = 1

stdio.writeln('Longest run: ' + str(longest_run) + ' consecutive ' + str(int(number)) + 's')
        

    
    