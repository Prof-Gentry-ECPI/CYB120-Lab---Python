import datetime

def printheader():
print('Name: ' + List[0])
print('Department: ' + List[1])
print('Computer: ' + List[2])
print('Date and Time: ' + DateAndTime)
print('Name of Report: ' + List[3])
    
def printfooter():
print('(c)     www.marhyn8894.com     '+ NameOfReport + '     Page 1 of 1')

List = []
InputLine = input('Enter name, Department, Computer, and Report Name: ')
if InputLine eq nothing:
print('Try again')

List = InputLine.split(",")
dateandtime = str(datetime.datetime.now())
                 
printheader()
print('\nReport goes here\n')
printfooter()
