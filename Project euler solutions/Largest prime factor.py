##Problem number 3

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#Solution - 6857

#Method 1 initial logic try
def primeFactorsM1(ran):
    #Making list for prime factors
    factors = []
    #Cutting computation by decreasing range by half
    for i in range(2, int(ran/2)):
        #Checking if i is a factor of the number specified
        if (ran%i == 0):
            #Checking if the factor is a prime number
            if(checkPrime(i) == True):
                #Appending prime factor into the list
                factors.append(i)
    #Returning largest prime factor
    return max(factors)

#Method 2 with solution for increased computation speed
def primeFactorsM2(ran):
    #Making a copy of the number specified
    num = ran
    #Making a list for prime factors
    factors = []
    #Initializing a counter
    count = 0
    #Making an infinite loop
    while True:
        #Checking numbers in the range of the number specified
        for i in range(2, int(num)+1):
            #Checking if i is a factor of the number specified 
            if(num%i == 0):
                #Checking if the number is a prime
               if (checkPrime(i) == True):
                    #Decresing the range for computation by the factor. This follows the prime factorization technique.
                    num = num/i
                    #Appending prime factor into the list
                    factors.append(i)
                    #Breaking the for loop after the smalled prime is found. This again follows the prime factorization technique.
                    break
            #Checking if for loop has iterated over the entire range of numbers
            if (i == num-1):
                #Increasing counter
                count = count + 1
        #If counter was increased and all factors were found, infinite loop is broken
        if count == 1:
            break
    #Returing the largest factor
    return max(factors)

#Function for checking if a number is prime
def checkPrime(num):
    #Iterating over all the values num
    for i in range(2, int(num/2)+1):
        #Checking if num has a factor
        if (num%i == 0):
            #Returning that the num is not a prime factor
            return False
    #Returning that the num is a prime factor after checking if any factors exist
    return True    

#Printing solution of method 2 
print(primeFactorsM2(600851475143))


