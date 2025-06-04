import datetime

def printheader():
    print(f'Name: {n}' \n'Dept{d}' \n'Comp:{c}' \n'Date: {dt}'\n'Report: {r}')
    
def printfooter():
    print(f'(c)     www.jamwit3278.com     '{r}'     Page 1 of 1')

InputLine = input('Nam, Dept, Comp, and Report: ')
if InputLine == '':
    print('Try again')
    InputLine = input('Nam, Dept, Comp, and Report: ')

n, d, c, r = InputLine.split(",")
dt = datetime.date.time.now
                 
printheader()
print('\nReport goes here\n')
printfooter()
