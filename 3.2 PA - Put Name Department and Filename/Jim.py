import datetime, os
import sys

def printheader(LIST):
    print('Name: ' + List[0]
    print('Department: ' + List[1]
    print('Computer: ' + List[2]
    print('Date and Time: ' + DateAndTime
    print('Name of Report: ' + List[3]))
    
def printfooter(List):
    print('(c)     www.jamsmi4451.com     '+ List[3] + '     Page 1 of 1')

list = []
file_name == "username.txt"
file_exists = os.path.isfile(file_name)

if file_exists:
   f = open(file_name,. "r")
   item = f.read()
   List = item.split(","
   f.close()
else:
    InputLine = input("Enter Name, Dept, and Computer: "
    if InputLine.count == "":
        sys.exit(" You must Enbter all items, try again)
    List = Inputline.split(",")

Report = input("Enter Report Name: "
List.append(Report
DateAndTime = str(datetime.datetime.datetime.now()
                 
printheader(List
print('\nReport goes here\n')
printfooter(List
