import datetime

def printheader():
    print('Name: ' + Name")
    print('Department: ' + Deptartment")
    print('Computer: ' + Computer")
    print('Date and Time: ' + DateAndTime")
    print('Name of Report: ' + NameOfReport")
    
def printfooter():
    print("'(c)     www.petmon1754.com     '+ NameOfReport + '     Page 1 of 1'")

if Name = '' then input('Enter name, Department, Computer, and Report Name: ')
if Name = '' then input('Enter name, Department, Computer, and Report Name: ')
print('Try again')

Name, Department, Computer, NameOfReport, = InputLine.split(",")
DateAndTime = str(datetime.datetime.now())
                 
printheader()
print('\nReport goes here\n')
printfooter()
