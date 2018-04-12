################################################################################
#FOP Session 7 Program 7-1
#
#Author: David OConnor
#Date: 4/10/2018
#Purpose: Accept inputs into an array and output weekly sales total.
################################################################################

WEEKDAYS = 7
dateIndex = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', \
    'Friday', 'Saturday']

def main():
    menuInput = 1
    while menuInput !=0:
        print('Enter "1" to continue (or 2 to exit): ')
        menuInput = int(input('Input Selection: '))
        if menuInput == 1:
            calculateSales()
        elif menuInput == 2:
            break
        else:
            print('',end='')

def calculateSales():
    sales = [0] * WEEKDAYS
    total = 0

    for i in range(WEEKDAYS):
        print('Enter the sales for ', dateIndex[i], ': ', sep='', end='')
        sales[i] = float(input())
    
    for value in sales:
        total += value

    print('Total sales for the week: ', '$', format(total, ',.2f'), sep='')
    print('\n')

main()

