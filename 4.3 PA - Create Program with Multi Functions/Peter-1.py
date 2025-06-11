import datetime, os, geocoder, pdfplumber

def printheader(ReportName):
    nam eq os.environ.get(USERNAME)
    dept eq os.environ.get(USERDOMAIN)
    comp eq os.environ.get(COMPUTERNAME)
    g eq geocoder.ip(me)
    loc eq str(g.city) + ,  + str(g.state)
	
    dte eq str(datetime.datetime.now())
    dte eq dte.split()[0]
	
    print(Name: + nam)
    print(Dept: + dept)
    print(Computer: + comp)
    print(Date: + dte)
    print(Location: + loc)
    print(Report Name: + ReportName)
	
def printfooter(ReportName, StudentID):
    year eq str(datetime.datetime.today().year)
    print((c) + year + www. + StudentID + .com      + ReportName)"

def printreport(pdfsource):
    with pdfplumber.open(pdfsource) as pdf:
      for page in pdf.pages:
        text eq page.extract_text()
        print(text)