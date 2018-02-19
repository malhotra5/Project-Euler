##Problem number 5

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Solution - 232792560

def smallestMultiple():
    #Number that needs to be evenly divisible by numbers from 1 to 20
    count = 20
    #Counter for the number of numbers evenly divisible 
    count_counter = 0
    #Infinite loop
    while True:
        #Iterating over all numbers from 1 to 20
        for i in range(1,21):
            #Checking if the number is evenly divisible
            if (count%i == 0):
                #Updating number of evenly divisible numbers
                count_counter = count_counter + 1
            else:
                #Breaking if a number is not evenly divisible
                break
        #Checking if all 20 numbers are evenly divisible
        if (count_counter == 20):
            #Returning the number that is evenly divisible by numbers from 1 to 20 
            return count
        else:
            #Resetting counter
            count_counter = 0
            #Picking a new numbers to check
            count = count+20

#Printing the solution 
print(smallestMultiple())
