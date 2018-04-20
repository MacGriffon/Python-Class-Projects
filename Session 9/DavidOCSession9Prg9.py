################################################################################
#FOP Session 9 Program 9-1
#Author: David OConnor
#Date: 
#Purpose: 
################################################################################

C:\Users\Maldon\AppData\Local\Programs\Python\Python36-32\python.exe
def main():
    menuInput = 0
    while menuInput == 0:
        print('Make a selection:\n1: Enter a Class Room Number. \
            \n2: Enter a Class Instructor.\n3: Enter a Class Meeting Time.\
            \n4: Exit.')
        menuInput=int(input('Selection: '))
        if menuInput == 1:
            enterClassroom()
            menuInput = 0
        elif menuInput == 2:
            enterInstructor()
            menuInput = 0
        elif menuInput == 3:
            enterTime()
            menuInput = 0
        elif menuInput == 4:
            applicationExit()
        else:
            menuInput = 0

def enterClassroom():
    print('option 1')
    
def enterInstructor():
    print('option 2')
    
def enterTime():
    print('option 3')
    
def applicationExit():
    SystemExit
    
main()
