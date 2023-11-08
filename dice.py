#Billy Boone
#09/15/23
#This program calculates dice probabilities and compares them to simulated results.

import random
import sys
import stdio
import stdarray

#Set trials to input
n = int(sys.argv[1])

#Function to calculate exact probabilities
def calculate_exact_probabilities():
    exact_probabilities = stdarray.create1D(13, 0.0) #Create array of size 13(0-12)
    for i in range(1, 7):   #First die roll
        for j in range(1, 7):  #Second die roll
            exact_probabilities[i + j] += 1.0  #Sum rolls and increment that index in the array(if sum was 5, index 5 would be incremented)
    for k in range(2, 13):
        exact_probabilities[k] /= 36.0 #Divide each index by 36 to get probability for each combination
    return exact_probabilities

#Function to calculate empirical probabilities
def calculate_empirical_probabilities(n):
    results = stdarray.create1D(13, 0) #Create array of size 13(0-12)
    for i in range(n): #Loop through the input number of trials
        dice1 = random.randint(1, 6)  #Number on first die
        dice2 = random.randint(1, 6)  #Number on second die
        results[dice1 + dice2] += 1   #Sum rolls and increment that index in results
    empirical_probabilities = []   #Create empty list to store probabilities
    for value in results[2:]:  #Loop through results array starting at index 2(There will be nothing at index 0 or 1)
        probability = value / n  #Get the probability of each value in results
        empirical_probabilities.append(probability) #Append the probability to the list
    return empirical_probabilities

exact_probabilites = calculate_exact_probabilities() #Call function to calculate exact probabilities

#Write results 
stdio.writeln("Exact results")
for i in range(2, 13):
    stdio.writeln(f"Probability the sum of die is {i}: {exact_probabilites[i]}")

empirical_probabilities = calculate_empirical_probabilities(n) #Call function to calculate empirical probabilities

#Write results
stdio.writeln("Empirical results")
for i in range(2, 13):
    stdio.writeln(f"Results the sum of die is {i}: {empirical_probabilities[i - 2]}")

#Write difference between exact and empirical results
stdio.writeln("Difference")
for i in range(2, 13):
    difference = empirical_probabilities[i - 2] - exact_probabilites[i]
    stdio.writeln(f"Difference when sum is {i}: {difference:.3f}")

#In order for the empirical results to be closer to the exact results, the number of trials must be increased. In my case it took 10,000,000 
#trials to match exact with empirical results to 3 decimal places. This threshold could be determined exactly with a while loop.
