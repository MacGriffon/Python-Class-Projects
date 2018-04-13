#######################################################################################
#FOP Session 6 Program 6-5
#
#Author: David OConnor
#Date: 3/25/2018
#Purpose: Read a file and output the sum or average of the numbers contained within.
#######################################################################################

def main():
    menuInput = 0
    while menuInput !=3:
        print('Select an option from the list below: \n1:Ruturn Total \
        \n2:Return Average \n3:Exit')
        menuInput = int(input('Input Selection: '))
        if menuInput == 1:
            returnTotal()
        elif menuInput == 2:
            returnAverage()
        elif menuInput == 3:
            break
        else:
            input('Invalid entry, press "Return" to continue...\n')

def readFileContents():
    count = 1
    infile = open('c:/devstuff/numbers.txt', 'r')
    line = infile.readline()
    total = 0
    try:
        while line !='\n' and line !=' \n' and line != '':
            print(str(count) + '\t' + format(int(line),',.1f') + '\n' ,end='')
            total += int(line)
            line = infile.readline()
            count += 1
        infile.close()
        return total, (count-1)
    except Exception as err:
        print(err)

def returnTotal():
    (total, count) = readFileContents()
    print('\nTotal:\t' + format(int(total),',.1f') + '\n')

def returnAverage():
    (total, count) = readFileContents()
    print('\nAverage:\t' + format(int(total/count),',.1f') + '\n')

main()
