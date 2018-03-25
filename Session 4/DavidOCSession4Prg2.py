#David OConnor
#FOP Session 4 Program 2
#Calculate C to F.

#Input for C.
celsiusInput = 1

while celsiusInput != 0000:
#Calculation for C to F from the internet. *Will do any temp from -40 to 40, for the winnipeg.*
    celsiusInput = int(input('Enter a Celsius value (Enter "0" to end): '))
    calculate = celsiusInput * 1.8 + 32

    print('Celsius          Fahrenheit')
    print('---------------------------')
    print(str(celsiusInput) + '               ' + str(calculate))
