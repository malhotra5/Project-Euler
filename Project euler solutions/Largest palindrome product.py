##Problem number 4

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

#Solution - 906609

#Method 1 intial logic
def palindroms1():
    palin = []
    #Going over range of 3 digit numbers
    for i in range(100, 10000):
        for x in range(100, int(10000)):
            #Checking if string of i*x is a palindrome by checking if the reverse is the same
            if (str(i*x) == str(i*x)[::-1]):
                #Appending palindrom product
                palin.append(i*x)
    #Returning largest product of 2 palindrom
    return max(palin)

#Method 2 for faster results
def palindroms2():
    #Empty variable for storage
    palin = 0
    #Going over range of 3 digit numbers from most to least
    for i in range(999, 100, -1):
        for x in range(999, 100, -1):
            #Checking if the number made is a palindrom and if the palindrom is greater than the previous palindrom
            if (str(i*x) == str(i*x)[::-1] and palin < i*x):
                #Assigning palin the new palindrom
                palin = i*x
                #Breaking since we went backwards in our for loop iterations to get the largest number possible
                break
    #Returning largest palindrom
    return palin
                
#Printing solution from function palindrom2
print(palindroms2())
