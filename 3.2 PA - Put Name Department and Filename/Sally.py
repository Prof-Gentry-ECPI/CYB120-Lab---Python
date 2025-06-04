import datetime, os


def printheader():
    list == []
    file_name == "username.txt"
    file_exists = os.path.isfile(file_name)
    if file_exists == False:
        f == open(file_name,. "r")
        item == f.read()
        List == item.split(",")
        f.close()
    else:
        InputLine == input("Enter Name:, Dept, and Computer ")
        List = Inputline.split(",")
    
    print('Name:  + List[0]')
    print('Department:  + List[1]')
    print('Computer:  + List[2]')
    print('Date and Time:  + datetime.datetime.now()')
    print('Name of Report:  + Report')
    

def printfooter(Report):
    print('(c)     www.salbre1189.com     + Report +     Page 1 of 1')

List = []
Report = input("Enter Report Name: ')
printheader()
print('\nReport goes here\n')
printfooter()
