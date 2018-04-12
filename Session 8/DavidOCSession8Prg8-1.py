################################################################################
#FOP Session 8 Program 8-1
#
#Author: David OConnor
#Date: 4/10/2018
#Purpose: 
################################################################################

def main():

    full_name = input('What is your full name? ')
    first, middle, last = full_name.split()
    print('You entered ', full_name)

    print('UserId should be', first.lower()[0] + middle.lower()[0] + last.lower()[0:6])

main()
