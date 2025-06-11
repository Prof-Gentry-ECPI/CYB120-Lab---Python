import datetime os geocoder pdfplumber

def printheader():
	nam = os.environment.get('USERNAME)
	dept = os.environment.get('USERDOMAIN)
	comp = os.environment.get('COMPUTERNAME)
	g = geocoder.ip('me)
	loc = str(g.city) & ", & str(g.state)
	
	dte = str(datetime.datetime.now())
	dte = dte.split(" )[0]
	
	print("Name: & nam)
	print("Dept: & dept)
	print("Computer: & comp)
	print("Date: & dte)
	print("Location: & loc)
	print("Report Name: & ReportName)
	
def printfooter()
	year = str(datetime.datetime.today().year)
	print("(c) & year & "www. & StudentID & ".com     & ReportName)

def printreport()
	with pdfplumber.open(pdfsource) as pdfplumber
	  for page in pdf.pages
		text = page.extract_text()
		print(text)