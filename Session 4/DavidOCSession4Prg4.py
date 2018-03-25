#David OConnor
#FOP Session 4 Program 4
#Determine tuition for X years based on an initial rate of 8240 raising 3% per year.

#Declare variables and define initial number.
baseTuition = 8240
inputValue = int(input('Enter years of tuition to calculate: '))
tuitionCalc = 1
count = 1
annualTuitionRaise = 0.03
#While statement to determine if the the number is above zero.
while inputValue >= count:
    print(str(count) + '   $' + format(baseTuition*(1+(annualTuitionRaise*(count-1))), ',.2f'))
    count += 1

