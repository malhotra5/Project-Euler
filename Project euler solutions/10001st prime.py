##Problem number 7

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

#Solution - 104743

#Function to get 10001 prime
def prime():
    #Making a counter
    count = 0
    #Holding the value of a prime number
    num = 1
    #Infinite loop
    while True:
        #Updating the value
        num = num + 1
        #Getting a result of as to whether num is prime
        res = checkPrime(num)
        #Checking if num is prime
        if(res == True):
            #Updating the prime number count
            count = count + 1
        #Checking if count has reached 10001
        if (count == 10001):
            #Returning 10001 prime
            return num

#Function to check if num is prime
def checkPrime(num):
    #Iterating over 2 to half the range of the number
    for i in range(2, int(num/2)+1):
        #Checking if the number is evenly divisible
        if (num%i == 0):
            #Returning that the number is not a prime
            return False
    #After iterating, returning that the number is a prime
    return True

#Printing the solution
print(prime())
