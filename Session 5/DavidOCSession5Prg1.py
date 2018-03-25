################################################################################
#FOP Session 5 Program 1
#
#Author: David OConnor
#Date: 02/22/2018
#Purpose: Paired program #1
################################################################################


#Declare constants.
RISE_PER_YEAR = 1.8


#Declare variables.
rise = 0.0


#Logic which does stuff.



#Outputs
# Calculate and print value for the rise each year.
print ('Year\t\tRise (in millimeters)')
print ('------------------------------------------')



for year in range(0,25):
    rise = rise + RISE_PER_YEAR
    print ((year + 1), '\t\t', format(rise, '.2f'))



