################################################################################
#FOP Session 5 Program 5-18
#
#Author: David OConnor
#Date: 2/28/2018
#Purpose: Check numbers 0-100 for prime numbers. Display results.
################################################################################

def main():
    print('number "x" is prime?')
    getInput()

#Loop 0 to 100 to determine prime state. Functions inside of functions OMG.
def getInput():
    testValue = 0
    for testValue in range (testValue,100):
        testValue += 1
        primeCheck=(determinePrime(testValue))
        output(testValue,primeCheck)
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
def output(testValue,primeCheck):
    if(primeCheck == 0):
        print(str(testValue) + " is prime")
    else:
        print(str(testValue) + " is not prime")

#Make things happen
main()
