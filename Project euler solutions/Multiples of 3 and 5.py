##Problem number 1

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#Solution - 233168

def findMultSum(rang):
    #Making a list for multiples of 3 and 5
    nums = []
    #Interating over the range in which we need to find multiples of 3 and 5
    for i in range(rang):
        #Checking if the number is a multiple of 3 or 5
        if(i%3 == 0 or i%5 == 0):
            #If the number already exists then pass as we don't want any repeats like 15 which is a multiple of both 3 and 5
            if i in nums:
                pass
            else:
                #Put the new number in the list
                nums.append(i)
    sumed = 0
    #Sum all the numbers in the list
    for i in nums:
        sumed = sumed + i
    #Return sum
    return sumed

#Printing solution
print(findMultSum)


