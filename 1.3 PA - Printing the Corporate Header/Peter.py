def printheader()
  string Name, Department, Computer, DateAndTime, NameOfReport

  Name eq 'Peter'
  Department eq 'IT'
  Computer eq 'Custom 5350x'
  DateAndTime eq '6/21/2022 4:45pm'
  NameOfReport eq 'A Great Report'

  print 'Name: ' & Name
  print 'Department: ' & Department
  print 'Computer: ' & Computer
  print 'Date and Time: ' & DateAndTime
  print 'Name of Report: ' & NameOfReport

def printfooter():
  print '(c) www.petmon1754.com     A Great Report     Page 1 of 1'

printheader()
print'\nReport goes here\n'
printfooter()
