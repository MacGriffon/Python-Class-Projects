import datetime
now = datetime.datetime.now()
name = str()
course = str()

name = input("What's your name? ")
course = input("What course is this? ")
print ("Hi " + name +"! Welcome to " + course)
print ("I am running at " + str(now))
print ("That date format might be a little TMI.")
print ("Maybe I'll say I am running at " + now.strftime("%Y-%m-%d %H:%M"))
input ("Press the 'ENTER' key to close!")
