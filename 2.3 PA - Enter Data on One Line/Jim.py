import datetime
import sys

def printheader(LIST):
    print('Name: ') + List[0]
    print('Department: ') + List[1]
    print('Computer: ') + List[2]
    print('Date and Time: ') + DateAndTime
    print('Name of Report: ') + List[3]
    
def printfooter(list):
    print('(c)     www.jamsmi4451.com     '+ List[3] + '     Page 1 of 1')

List = []
InputLine = input('Enter name, Department, Computer, and Report Name: ')
if InputLine.count = "":
        sys.exit(" You must enter all items, try again)

List = InputLine.split(",")
DateAndTime = str(datetime.datetime.now())
                 
printheader(LIST)
print('\nReport goes here\n')
printfooter(list)
