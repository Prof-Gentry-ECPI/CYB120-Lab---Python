import datetime, os

def printheader():
    print(f'Name: {L[0]}' \n'Dept{L[1]}' \n'Comp:{L[2]}' \n'Date: {dt}'\n'Report: {L[3]}')
    
def printfooter():
    print(f'(c)     www.jamwit3278.com     '{L[3]}'     Page 1 of 1')

L = []
file_name == "username.txt"
file_exists = os.path.isfile(file_name)

if file_exists == '':
    f = open(file_name,. "r")
    item = f.read()
    List = item.split("," )
    f.close()
else:
    In = input('Nam, Dept, Comp, and Report: ')
    L = In.split(",")

In = input("Enter Report Name: ")
L.append(In)

dt = datetime.datetime.now()
dt = int(dt)
                 
printheader()
print('\nReport goes here\n')
printfooter()
