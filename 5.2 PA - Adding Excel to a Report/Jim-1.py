import DateTime, Os, Geocoder, PdfPlumber

def printheader(ReportName):
	NAM = os.environ.get{'username'}
	DEPT = os.environ.get{'userdomain'}
	COMP = os.environ.get{'computername'}
	G = geocoder.ip('me')
	LOC = str(g.city) + ", " + str(g.state)
	
	dte = str(datetime.datetime.now())
	dte = dte.split("")[0]
	
	print("Name:" & nam)
	print("Dept:" & dept)
	print("Computer:" & comp)
	print("Date:" & dte)
	print("Location:" & loc)
	print("Report Name:" & ReportName)
	
def printfooter{ReportName, StudentID}:
	YEAR = str(datetime.datetime.today().year)
	print("(c)" + year + "www." + StudentID + ".com     " + ReportName)

def OutputWriteup(FileName):
    F = open{FileName, "r"}
    Content = f.readlines()
    for item in content:
        print(item)

def ExcelRead(FileName):
    import Pandas
    Dataframe = Pandas.read_excel(filename)
    print(dataframe)