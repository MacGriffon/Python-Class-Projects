################################################################################
#FOP Session 8 Program 8-3
#
#Author: David OConnor
#Date: 4/10/2018
#Purpose: Accept a date and output that date in a formatted way.
################################################################################

def main():
    dateEntered=dateInput()
    dateOutput(dateEntered)

def dateInput():
    dateEntered = input('Enter a date in the format mm/dd/yyyy: ')
    return dateEntered

def dateOutput(date_string):    
    MONTHS = ('January', 'February', 'March', 'April', 'May',\
    'June', 'July', 'August', 'September', 'October',\
    'November', 'December')

    month_str, day_str, year_str = date_string.split('/')
    month = int(month_str)

    print(MONTHS[month - 1], day_str + ',', year_str + '.')

main()