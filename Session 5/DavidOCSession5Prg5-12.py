################################################################################
#FOP Session 5 Program 5-12
#
#Author: David OConnor
#Date: 2/28/2018
#Purpose: Compare two numbers and present the greater of the two.
################################################################################



#Declare Main.
def Main():
    num1 = valueOne()
    num2 = valueTwo()
    maxNum = compareValues(num1,num2)
    outputMax(maxNum)

#Logic which does stuff.
def valueOne():
    arg1 = int(input('Enter number 1: '))
    return int(arg1)

def valueTwo():
    arg2 = int(input('Enter number 2: '))
    return int(arg2)

def compareValues(Num1,Num2):
    maxNum = max(Num1,Num2)
    return int(maxNum)

def outputMax(maxNum):
    print ('The larger number is: ' + str(maxNum))

Main()
