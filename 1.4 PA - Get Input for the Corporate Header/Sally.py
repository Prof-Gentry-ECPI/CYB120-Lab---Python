def printheader():
  input('Name? ')
  input('Department? ')
  input('Computer? ')
  input('Date and Time? ')
  if Name is blank:
    print('try again')
    break

  print('Name: ' + Name)
  print('Department: ' + Dept)
  print('Computer: ' + Comp)
  print('Date and Time: ' + Date)
  print('Name of Report: ' + Report)

def printfooter():
  print(' (c) www.salbre1189.com     " + Report + "     Page 1 of 1')

Report = printheader()
print("\nReport goes here\n')
printfooter(Rept)
