################################################################################
#FOP Session 7 Program 7-3
#
#Author: David OConnor
#Date: 4/10/2018
#Purpose: Accept rainfall data and output metrics.
################################################################################

NUM_MONTHS = 12
menuInput = 1
MONTHS = ['January', 'February', 'March', 'April', 'May',\
             'June', 'July', 'August', 'September', 'October',\
             'November', 'December']

def main():
    rainMax,rainMin,rainAverage,total = rainfallCalc()
    rainOutput(rainMax,rainMin,rainAverage,total)

def rainfallCalc():
    rainfall = [0] * NUM_MONTHS
    rainTotal = 0

    for i in range(NUM_MONTHS):
        print('Enter the rainfall for ', MONTHS[i], ': ', sep='', end='')
        rainfall[i] = float(input())
    
    for value in rainfall:
        rainTotal += value

    rainMax = MONTHS[rainfall.index(max(rainfall))]
    rainMin = MONTHS[rainfall.index(min(rainfall))]
    rainAverage = rainTotal / len(rainfall)

    return rainMax,rainMin,rainAverage,rainTotal

def rainOutput(rainMax,rainMin,rainAverage,rainTotal):
    print('Total rainfall: ', format(rainTotal, ',.2f'), sep='')
    print('Average rainfall: ', format(rainAverage, ',.2f'), sep='')
    print('Highest rainfall: ', rainMax)
    print('Lowest rainfaull: ', rainMin)

main()