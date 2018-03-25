#David OConnor
#FOP Session 3 Program 2
#Roman numeral translator

#Define minimum and maximum values accepted by the application.
MINIMUM_VALUE = 1
MAXIMUM_VALUE = 10

#Request input from user between the min and max values.
number = int(input('Enter a number between 1 and 10: '))

#Validate that the number entered is within the acceptable range and provide feedback for invalid entries.
if number < MINIMUM_VALUE or number > MAXIMUM_VALUE:
    print('Invalid entry. You entered a number which is not within the specified range.')
#Produce output based on the number entered.
elif number == 1:
    print('I')
elif number == 2:
    print('II')
elif number == 3:
    print('III')
elif number == 4:
    print('IV')
elif number == 5:
    print('V')
elif number == 6:
    print('VI')
elif number == 7:
    print('VII')
elif number == 8:
    print('VIII')
elif number == 9:
    print('IX')
elif number == 10:
    print('X')
