def printheader():
  print(f'Name: {n}\nDepartment: {d}\nComputer: {c}\nDate: {d}\nReport: {r}')

def printfooter():
  print(f'(c) www.jamwit3278.com     {r}     Page 1 of 1')

n = input('Enter Name: ')
d = input('Enter Department: ')
c = input('Enter Copmputer: ')
dt = input('Enter Date and Time: ')
r = input('Enter Name of report: ')

printheader()
print ('\nReport goes here\n')
printfooter()
