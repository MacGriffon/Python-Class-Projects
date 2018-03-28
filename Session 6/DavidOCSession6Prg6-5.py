################################################################################
#FOP Session 6 Program 6-5
#
#Author: David OConnor
#Date: 3/25/2018
#Purpose: Read a file and output the sum or average of the numbers contained within.
################################################################################

def main():
    returnTotal()
    returnAverage()

def readFileContents():
    count = 1
    infile = open('z:/numbers.txt', 'r')
    line = infile.readline()
    total = 0
    try:
        while line !='\n' and line !=' \n':
            print(str(count) + '\t' + format(int(line),',.1f') + '\n' ,end='')
            total += int(line)
            line = infile.readline()
            count += 1
        infile.close()
    except Exception as err:
        print(err)
    return total, count

def returnTotal():
    (total, count) = readFileContents()
    print('\nTotal:\t' + format(int(total),',.1f'))

def returnAverage():
    (total, count) = readFileContents()
    print('\nAverage:\t' + format(int(total/count),',.1f'))

main()
