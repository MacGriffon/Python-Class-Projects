################################################################################
#FOP Session 6 Program 6-5
#
#Author: David OConnor
#Date: 3/25/2018
#Purpose: Read a file and output the sum of the numbers contained within.
################################################################################

def main():
    infile = open('z:/numbers.txt', 'r')
    line = infile.readline()
    while line:
        print(line,end='')
        line = infile.readline()
    infile.close()
    # print(str(filesum))
#Make things happen
main()
