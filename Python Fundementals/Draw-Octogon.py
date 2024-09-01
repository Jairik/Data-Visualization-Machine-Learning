'''
Approach: When drawing the octogon, the program prints L (side legnth) asterisks, adding 1 to each 
side after L iterations. Then, the program will print L+((L-1)*2) asterisks L-2 times. Then, it will 
do the first step in reverse. This strategy breaks up the octogon into 3 pieces, which is more managable.
EDIT: Base cases had to be considered for side lengths of 2 & 3 due to out of bounds errors
'''

#Get and validate the octogon length
valid = False
while not valid:
    L = int(input("Enter Octogon Side Length: "))
    if L < 2:
        print("ERROR- Please try again with a valid number")
    else:
        valid = True #continue to next step
        
#Defining side lengths at crucial points
num_asterisks_top = L
num_asterisks_middle = (L*3)-2

#List to store the different rows
octogon = []

#Loading top portion of octogon onto list
for i in range(0, L-1): 
    cur_row = []
    #Iteration from 0 to the max octogon size
    for j in range(1, num_asterisks_middle):
        if j < L-i or j >= L+L+i:
            cur_row.append(' ')
        else:
            cur_row.append('*')
    octogon.append(cur_row)

#Loading middle portion of octogon onto list
middle_row = []
for i in range(0, num_asterisks_middle):
    middle_row.append('*')
if L > 2:
    for i in range(0, L-2):
        octogon.append(middle_row)
else: #Base case for L of 2
    octogon.append(middle_row)
    
#Loading bottom portion of octogon onto list (inverse of top)
if L > 3:
    for i in range(0, L+1):
        octogon.append(octogon[L-i])
else: #Base case if L > 3
    if L == 3:
        octogon.append(octogon[1])
    octogon.append(octogon[0])
    
#Print the octogon 
for sublist in octogon:
    print(' '.join(map(str, sublist))) #Print can be changed to '' for tighter shape