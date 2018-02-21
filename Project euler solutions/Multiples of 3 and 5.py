##Problem number 1

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#Solution - 233168

def findSum(rang):
    #Interating over the range in which we need to find multiples of 3 and 5
    for i in range(rang):
        #Checking if the number is a multiple of 3 or 5
        if(i%3 == 0 or i%5 == 0):
            #If it is, adding it to the summ of all the previous multiples of 3 and 5.
            summ = summ + i
            
    return summ

#Printing solution
print(findSum)


