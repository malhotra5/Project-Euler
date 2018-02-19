##Problem number 10

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

#Solution - 142913828922

#Bugs - Have not found an efficient way to reduce computation time.


def primes(num):
    for i in range(2, int(num/2)+1):
        if (num%i == 0):
            return False
    return True
def addprimes():
    sums = 0
    num = 2000000
    counter = 2
    while True:
        res = primes(counter)
        if res == True:
            sums = sums + counter
        if counter == num/2:
            break
        counter = counter + 1
        
    return sums
print(addprimes())

