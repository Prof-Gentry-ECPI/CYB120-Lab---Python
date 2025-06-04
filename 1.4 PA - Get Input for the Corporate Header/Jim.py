import sys

def printheader(name, department, Computer, DateAndTime, NameofReport:
  print('Name: ' + Name
  print('Department: ' + Department
  print('Computer: ' + computer
  print('Date and Time: ' + Dateandtime
  print('Name of Report: '+ Nameofreport

def printFooter(NameOfReport:
  Print('(c) www.jamsmi4451.com     ' + NameOfReport + '     Page 1 of 1'

Name = input('Enter Name: '
Department = input ('Enter Department: '
Computer = input ('Enter Computer: '
DateAndTime = input('Enter Date and Time: '
NameOfReprot = input('Enter Name of report: '
if Name == '' or Department == '' or Computer == '':
  sys.exit('You must answer all questions, try again')

printheader{Name, Department, DateAndTime, NameOfReport, Computer}
print('\nreport goes here\n'
printfooter(NameOfReport
