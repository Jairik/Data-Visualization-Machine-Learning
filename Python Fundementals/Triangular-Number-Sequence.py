'''
Approach: The clear pattern that I see is that the number of dots corresponding to the triangle
is simply a summation of all previous rows. For example, to calculate a triangle with 4 rows, we 
add the number of dots of the previous triangle (1+2+3) plus the current triangle (6+4=10), which
meets our test case
'''

#Generalized equation that could be used for any summation
def series(n, first_num):
    return n * ((first_num + n) / 2)

#Helper function to determine number of dots for given integer, printing and returning the result
def calculate_dots(n):
    first_num: int = 1 #Known in this case
    cur_dots: int = int(series(n, first_num))
    print(cur_dots, end=', ')
    return cur_dots

even_nums = []
odd_nums = []

for i in range(1, 21):
    if i%2 == 0: #even case
        even_nums.append(calculate_dots(i))
    else: #odd case
        odd_nums.append(calculate_dots(i))

#Find the sums of the even and odd lists
print() #Newline
print("Sum of Even Numbers: ", sum(even_nums))
print("Sum of Odd Numbers: ", sum(odd_nums))
