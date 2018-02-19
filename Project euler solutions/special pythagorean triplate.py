## Problem number 9

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#                                                                 a2 + b2 = c2
#For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#Solution - 31875000

#Import math to square numbers
import math
#Iterate over 3 to 1000 for values of a
for i in range(3,1000):
    #Iterate over 3 to 1000 for values of b 
    for x in range(3,1000):
        #To make results faster
        if x + i > 997:
            break
        #Calculate the value of c
        num3 = math.sqrt(i**2 + x** 2)
        #Check if the values add up to 1000
        if(num3 + i + x == 1000):
            #Print a,b and c
            print(x, i, num3)
            #Print the product of a,b and c
            print(x*num3*i)
