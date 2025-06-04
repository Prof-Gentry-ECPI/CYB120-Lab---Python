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
file_name == "username.txt"
file_exists = os.path.isfile(file_name)

if file_exists eq False:
f = open(file_name,. "r")
item = f.read()
List = item.split("," )
f.close()
else:
print("Create your user file and try again")
sys.exit()

Report = input("Enter Report Name: ")
List.append(Report)
dateandtime = str(datetime.datetime.now())
                 
printheader()
print('\nReport goes here\n')
printfooter()
