class Person:
    person_name = "Fred"
    person_age = 50

    def Say_Hello(self):
        print("hello!!")

def main():
    student = Person()

    student.Say_Hello()
    print ('My age is', student.person_age, 'test')

main()