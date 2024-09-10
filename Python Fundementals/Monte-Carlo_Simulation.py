'''
Approach: Create a blank dictionary, then iterate the number by one to determine total
occurances. Dice will be rolled n times by generating a random number from 1-6 twice, then summed.
Probabilities will be printed at the end.
'''

from random import randint as rand #library to acheive "random" dice roll
import pandas as pd #For printing the table of values

#Defining a function to roll the dice
def roll():
    return (rand(1, 6) + rand(1, 6))

#Getting user input
n = int(input("How many times should I roll the dice? "))

#Defining empty dictionary to hold values
occurances = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}

#Rolling the dice n times
for i in range(n):
    val = roll()
    occurances[val] = occurances[val] + 1

#Calculating the Probabilities
propabilities = occurances
for j in range(2, 13):
    total_occurances = occurances[j] #Handling potential key value error
    propabilities[j] = str(round((total_occurances/n)*100, 2))+ '%'

#Convert to pandas dataframe for cleaner print statement (i love pandas)
propabilities_df = pd.DataFrame(list(propabilities.items()), columns=['Total', 'Probability'])
title = "Probabilities for " + str(n) + " rolls"



print('\n', title)
print(propabilities_df.to_string(index=False))
print() #Empty Line
