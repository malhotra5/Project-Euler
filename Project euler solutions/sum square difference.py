##Problem number 6

#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#Solution - 25164150

#Importing math for squaring
import math

def sumSquareDif():
    #Value of sum then square
    sumSqr = 0
    #Value of square then sum
    Sqrsum = 0
    #Iterating over 1 to 100
    for i in range(1,101):
        #Adding all the values
        sumSqr = sumSqr + i
        #Adding the square
        Sqrsum = Sqrsum + i**2
    #Squaring the sum
    sumSqr = sumSqr**2
    #Returning the difference
    return sumSqr - Sqrsum

#Printing the solution
print(sumSquareDif())
