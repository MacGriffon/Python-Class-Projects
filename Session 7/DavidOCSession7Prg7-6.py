################################################################################
#FOP Session 7 Program 7-6
#
#Author: David OConnor
#Date: 4/9/2018
#Purpose: Display a list of numbers higher than a user input number.
################################################################################

def main():
    menuInput = 0
    while menuInput !=99:
        NUMBER_INDEX = [1,2,3,4,5,6,7,8,9,10]
        print('1:Enter an integer between 1 and 10 (or 99 to exit): ')
        menuInput = int(input('Input Selection: '))
        if menuInput >= 1 and menuInput <= 10:
            displayList(NUMBER_INDEX)
            listAboveSelection(NUMBER_INDEX,menuInput)
        elif menuInput == 99:
            break
        else:
            print('',end='')

def displayList(NUMBER_INDEX):
    print(NUMBER_INDEX)

def listAboveSelection(NUMBER_INDEX,menuInput):
    del NUMBER_INDEX[0:menuInput]
    print(NUMBER_INDEX)

main()
