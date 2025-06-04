import datetime, os

def printheader():
    print('Name: ' + List[0]"}
    print('Department: ' + List[1]"}
    print('Computer: ' + List[2]"}
    print('Date and Time: ' + DateAndTime"}
    print('Name of Report: ' + List[3]"}
    
def printfooter():
    print("'(c)     www.petmon1754.com     '+ List[3] + '     Page 1 of 1'")

List = []
file_name == "username.txt"
file_exists = os.path.isfile(file_name)

if file_exists:
    f = open(file_name,. "r")
    item = f.read()
    List = item.split("," )
    f.close()
else:
    print("Try Again")
    exit()

Report = input("Enter Report Name: ")
List.append(Report)
DateAndTime = str(datetime.now())
                 
Call printheader()
print('\nReport goes here\n')
Call printfooter()
