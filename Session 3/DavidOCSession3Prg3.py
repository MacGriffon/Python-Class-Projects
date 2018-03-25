#David OConnor
#FOP Session 3 Program 1
#Software package price calculator.

#Input for the number of software packages ordered.
packagesPurchased = int(input('Enter the number of packages purchased:'))
#Define Non magic number of default package price.
basePackagePrice = 99

#Define discounts.
discountZeroPercent      = 0.00
discountTenPercent       = 0.10
discountTwentyPercent    = 0.20
discountThirtyPercent    = 0.30
discountFourtyPercent    = 0.40

discountZeroPercentQty   = 10
discountTenPercentQty    = 20
discountTwentyPercentQty = 50
discountThirtyPercentQty = 100

#Define Output Values
discountTotal =0.0
totalPrice =0.0

2#Determine Discount Percentage and calculate totals. Output.
if packagesPurchased < discountZeroPercentQty:
    discountTotal = discountZeroPercent
    totalPrice = packagesPurchased * basePackagePrice - discountTotal
    print('Discount rate is: ' + str('{:.2%}'.format(0.0)))
    
if packagesPurchased in range(discountZeroPercentQty,discountTenPercentQty):
    discountTotal = packagesPurchased * basePackagePrice * discountTenPercent
    totalPrice = packagesPurchased * basePackagePrice - discountTotal
    print('Discount rate is: ' + str('{:.2%}'.format(0.1)))
    
if packagesPurchased in range(discountTenPercentQty,discountTwentyPercentQty):
    discountTotal = packagesPurchased * basePackagePrice * discountTwentyPercent
    totalPrice = packagesPurchased * basePackagePrice - discountTotal
    print('Discount rate is: ' + str('{:.2%}'.format(0.2)))
    
if packagesPurchased in range(discountTwentyPercentQty,discountThirtyPercentQty):
    discountTotal = packagesPurchased * basePackagePrice * discountThirtyPercent
    totalPrice = packagesPurchased * basePackagePrice - discountTotal
    print('Discount rate is: ' + str('{:.2%}'.format(0.3)))
    
if packagesPurchased >= discountThirtyPercentQty:
    discountTotal = packagesPurchased * basePackagePrice * discountFourtyPercent
    totalPrice = packagesPurchased * basePackagePrice - discountTotal
    print('Discount rate is: ' + str('{:.2%}'.format(0.4)))
    

print('Discount Amount: $' + format(discountTotal, ",.2f"))
print('Total Amount: $' + format(totalPrice, ",.2f"))
