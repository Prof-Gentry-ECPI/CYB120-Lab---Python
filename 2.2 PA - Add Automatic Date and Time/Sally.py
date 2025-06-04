import datetime

def printheader():
    InputLine = input('Enter Name, Department, Computer, and Report Name: ')
    if InpurLine == "":
        print("Try again")
        input('Enter Name, Department, Computer and Report Name: ')

    Name, Department, Computer, NameOfReport = InputLine.split(",")
    DateAnTime = str(datetime.datetime.now())

    print('Name: ' + Nam)
    print('Department: ' + Dept)
    print('Computer: ' + Comp)
    print('Date and Time: ' + DateAnddTime)
    print('Name of Report: ' + Report)
    return Report

def printfooter(Report):
    print('(c)     www.salbre1189.com     '+ NameOfReport + '     Page 1 of 1')

NameOfReport = printheader()
print('\nReport goes here\n')
printfooter(Report)
