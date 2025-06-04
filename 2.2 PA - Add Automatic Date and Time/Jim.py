import datetime
import sys

def printheader(name, department, Computer, DateAndTime, NameofReport:
    print('Name: ') + Name
    print('Department: ') + Deptartment
    print('Computer: ') + Computer
    print('Date and Time: ') + DateAndTime
    print('Name of Report: ') + NameofReport
    
def printfooter(NameofReport:
    print('(c)     www.jamsmi4451.com     '+ NameOfReport + '     Page 1 of 1')

InputLine = input('Enter name, Department, Computer, and Report Name: ')
  if InputLine = "":
        sys.exit(" You must enter all items, try again:)

Name, Department, Computer, NameOfReport, = InputLine.split(",")
DateAndTime = str(datetime.datetime.now())
                 
printheader(name, department, Computer, DateAndTime, NameofReport)
print('\nReport goes here\n')
printfooter(NameOfReport
