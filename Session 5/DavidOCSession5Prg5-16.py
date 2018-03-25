################################################################################
#FOP Session 5 Program 5-16
#
#Author: David OConnor
#Date: 2/28/2018
#Purpose: Determine results of 100 random number rolls.
################################################################################
from random import randint
evenNumbers = 0
oddNumbers = 0

for LCV in range(0,10000):
    num=(randint(0, 1000))
    if (num % 2 == 0):
        evenNumbers += 1
    else:
        oddNumbers += 1

print ('Out of 100 random numbers, ' + str(evenNumbers) \
       + ' were even, and '  + str(oddNumbers) + ' were odd.')

