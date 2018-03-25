################################################################################
#FOP Session 5 Program 5-17
#
#Author: David OConnor
#Date: 2/28/2018
#Purpose: Determine if an input number is prime or not.
################################################################################

def main():
    testValue=(getInput())
    primeCheck=(determinePrime(testValue))
    output(primeCheck)

#Get input from user to test if prime.
def getInput():
    testValue = int(input("Enter a number: "))
    return int(testValue)

#Check the provided value to see if it is a prime number.
def determinePrime(testValue):
    primeCheck=0

    if testValue > 3: #1-3 are assumed to be prime
        for x in range(2,testValue):
            if (testValue % x) == 0:
                primeCheck += 1
                break
    return primeCheck

#Validate output from the prime check function and display result.
def output(primeCheck):
    if(primeCheck == 0):
        print("Number is prime")
    else:
        print("Number is not prime")

#Make things happen
main()

