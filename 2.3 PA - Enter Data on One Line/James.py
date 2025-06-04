import datetime

def printheader():
    print(f'Name: {L[0]}' \n'Dept{L[1]}' \n'Comp:{L[2]}' \n'Date: {dt}'\n'Report: {L[3]}')
    
def printfooter():
    print(f'(c)     www.jamwit3278.com     '{L[3]}'     Page 1 of 1')

L = []
In = input('Nam, Dept, Comp, and Report: ')
if In == '':
    print('Try again')
    In = input('Nam, Dept, Comp, and Report: ')


L = In.split(",")
dt = datetime.datetime.now()
dt = int(dt)
                 
printheader()
print('\nReport goes here\n')
printfooter()
