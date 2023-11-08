#Billy Boone
#09/13/23
#This program is a simulation for the amount of children a family will have 
#assuming they are going for at least 1 of each gender. Each trial is one test.

#Import modules
import random
import sys 
import stdio
import stdarray


#Set trials to input
trials = int(sys.argv[1])

#Assign variables with arrays the size of trials
avg_children = stdarray.create1D(trials, 0)
two_children = stdarray.create1D(trials, 0)
three_children = stdarray.create1D(trials, 0)
four_children = stdarray.create1D(trials, 0)
fiveormore_children = stdarray.create1D(trials, 0)


#Run trials and update arrays with respective values
for trial in range(trials):
    attempts = 0
    boys = 0
    girls = 0
    while boys == 0 or girls == 0:
        r = random.randrange(2)
        if r == 0:
            boys += 1
        else:
            girls += 1
        attempts += 1
    avg_children[trial] = attempts
    if attempts == 2:
        two_children[trial] = 1
    elif attempts == 3:
        three_children[trial] = 1
    elif attempts == 4:
        four_children[trial] = 1
    elif attempts >= 5:
        fiveormore_children[trial] = 1
    

#Write results.

stdio.writeln('Average # children: ' + str(round(sum(avg_children) / trials)))
stdio.writeln('Trials with 2 children: ' + str(sum(two_children)))
stdio.writeln('Trials with 3 children: ' + str(sum(three_children)))
stdio.writeln('Trials with 4 children: ' + str(sum(four_children)))
stdio.writeln('Trials with 5 or more children: ' + str(sum(fiveormore_children)))


