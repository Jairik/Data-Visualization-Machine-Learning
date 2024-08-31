'''
Approach: When drawing the octogon, the program prints L (side legnth) asterisks, adding 1 to each 
side after L iterations. Then, the program will print L+((L-1)*2) asterisks L-2 times. Then, it will 
do the first step in reverse

Difficulties: How to calculate spaces
    Going Down
        L-1-i Spaces
        
    Going Up
        i-1 Spaces
        
*** NOTE TO SELF: ***
Since i in range() wouldn't have 0-based indexing, I dont think I need to subtract 1 from anything (sweet!)

Thought-dump for tmr: 
for i in range (1, L)
    print L + (i-1)*2 Asterisks
    ^ Fill the rest in blanks
    
for j in range (1, L-1)
    print L + (L-1)*2 asterisks
    
for k in range (1, L)
    print L + ((L-1-i)*2 asterisks (I think)
    
boom done
'''