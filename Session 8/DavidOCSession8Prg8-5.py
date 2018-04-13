################################################################################
#FOP Session 8 Program 8-5
#
#Author: David OConnor
#Date: 4/10/2018
#Purpose: Accept a phone number and output it.
################################################################################

def main():
    phone_number = input('Enter the telephone number in the format XXX-XXX-XXXX: ')
    split_number = phone_number.split('-')

    special_char = False
    count = 0
    phone_list = ''

    while special_char == False and count < 3:
        for ch in split_number[count]:
            if ch.isdigit():
                phone_list += ch
            elif ch.upper() in 'ABC':
                phone_list += '2'
            elif ch.upper() in 'DEF':
                phone_list += '3'
            elif ch.upper() in 'GHI':
                phone_list += '4'
            elif ch.upper() in 'JKL':
                phone_list += '5'
            elif ch.upper() in 'MNO':
                phone_list += '6'
            elif ch.upper() in 'PQRS':
                phone_list += '7'
            elif ch.upper() in 'TUV':
                phone_list += '8'
            elif ch.upper() in 'WXYZ':
                phone_list += '9'
            else:
                special_char = True
        if count != 2:
            phone_list += '-'
        count += 1

    if special_char:
        print('Please use alphanumeric values.')

    else:
        print('The phone number is', phone_list)

main()