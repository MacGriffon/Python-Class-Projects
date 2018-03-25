################################################################################
#FOP Session 5 Program 2
#
#Author: David OConnor / Colleen / Jon
#Date: 02/22/2018
#Purpose: Calculate weight loss over time.
################################################################################


#Declare constants/functions.
MONTHS = 1
MONTHLY_WT_LOSS = 4

def Main():
    weight = int(input('What is your starting weight?: '))
    weight_calc(weight)
    

def weight_calc(wtc):
    MONTHS = 1
    while MONTHS < 7:
        wtc = output_calc(wtc)
        print('At the end of month ' + str(MONTHS) + \
          ' your weight will be ' + str(wtc))
        MONTHS += 1

def output_calc(wt):
    wt = wt - 4
    return(wt)

#Declare variables/inputs.
#weight =int(input('What is your starting weight?: '))


#Outputs

#while MONTHS < 7:
#    weight -= MONTHLY_WT_LOSS
#    print('At the end of month ' + str(MONTHS) + \
#          ' your weight will be ' + str(weight))
#    MONTHS += 1

#input('Hit return to end.')


Main()
