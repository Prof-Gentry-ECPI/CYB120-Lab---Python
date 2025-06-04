def printheader()
  print("Name: ' & Name")
  print("Department: ' & Department")
  print("Computer: ' & Copmputer")
  print("Date and Time: ' & DateAndTime")
  print("Name of Report: ' & NameOfReport")

def printfooter():
  print '(c) www.petmon1754.com     ' & NameOfReport & '     Page 1 of 1'

if Name = '' then Name = input("Enter Name: ")
if Department = '' then Department = input("Enter Department: ")
if Computer = '' then Computer = input("Enter Computer: ")
if DateAndTime = '' then DateAndTime = input("Enter Date and Time: ")
if NameOfReport = '' then NameOfReport = input("Enter Name of report: ")

printheader()
print'\nReport goes here\n'
printfooter()
