#David OConnor
#FOP Session 4 Program 3
#Sum of numbers until you enter a negative.

#Declare variables and define initial number.
sumOfNumbers = 0
inputValue = int(input('Enter a positive number (negative to quit): '))
sumOfNumbers = inputValue
#While statement to determine if the the number is above zero.
while inputValue >= 0:
#Loop which keeps adding to the sum.
    inputValue = int(input('Enter a positive number (negative to quit): '))
    if inputValue >= 0:
        sumOfNumbers += inputValue
#If to make sure the initial value was above zero. Prints sum.
if sumOfNumbers >= 0:
    print('Total = ' + str(sumOfNumbers))
