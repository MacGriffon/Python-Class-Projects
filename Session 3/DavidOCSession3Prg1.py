#David OConnor
#FOP Session 3 Program 1
#Wage calculator for regular/overtime pay.

#Define the variable for number of hours worked and ask user to input that data.
hoursWorked = float(input('Enter the total hours worked this week: '))
#Define the variable for number of hourly wage and ask user to input that data.
hourlyRate = float(input('Enter the hourly pay rate: '))
#Define constant variables.
maxRegularHours = 45
overtimeRate = 1.5

#Define calculated/boolean variables.
overTime = bool(False)
regularPay = 0.0
overtimePay = 0.0
grossPay = 0.0
hour = str(' hour')

#Calculate the variables.
if hoursWorked > maxRegularHours:
    overTime=True

if overTime:
    regularPay = (maxRegularHours * hourlyRate)
    overtimePay = ((hoursWorked - maxRegularHours) * (overtimeRate * hourlyRate))
    grossPay = (regularPay+overtimePay)
else:
    grossPay = (hoursWorked * hourlyRate)

if hoursWorked > (maxRegularHours+1):
    hour = str(' hours')

#Output wage calculation for normal pay without overtime.
print('\nYour gross pay is: $' + format(grossPay, ',.2f'), sep='')
#Output wage calculation with overtime pay.
if overTime:
    print('You received $' + format(overtimePay, ',.2f') + ' for the ' + \
          str(hoursWorked - maxRegularHours) + \
          str(hour) + ' of overtime' , sep='')

