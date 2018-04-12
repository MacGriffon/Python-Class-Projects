################################################################################
#FOP Session 8 Program 8-1
#
#Author: David OConnor
#Date: 4/10/2018
#Purpose: Accept a full name, break it apart, display with suggested username.
################################################################################

def main():
    full_name, first, middle, last = nameInput()
    usernameOutput(full_name, first, middle, last)

def nameInput():
    full_name = input('What is your full name? ')
    first, middle, last = full_name.split()

    return full_name, first, middle, last

def usernameOutput(full_name, first, middle, last):
    print('You entered ', full_name)
    print('UserId should be', first.lower()[0] + middle.lower()[0] + last.lower()[0:6])

main()
