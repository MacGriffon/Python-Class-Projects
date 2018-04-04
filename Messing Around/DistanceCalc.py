################################################################################
#Author: David OConnor
#Date: 
#Purpose: 
################################################################################

def main():
    (speed,time) = inputs()
    CalculationOuput(speed,time)

def inputs():
    speed = int(input('Speed in MPH: '))
    time = int(input('Time in Hours: '))
    return(speed,time)

def CalculationOuput(s,t):
    loop = 1
    for loop in range (1,t+1):
        print('Distance traveled is ' + str(int(loop) * int(s)) + ' miles in ' + str(loop) + 'hour(s).')
        loop += 1
#Make things happen

main()
