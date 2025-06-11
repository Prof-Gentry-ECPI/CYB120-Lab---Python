import datetime os geocoder pdfplumber

def printheader(n):
    n = os.environ.get('USERNAME')
    d = os.environ.get('USERDOMAIN')
    c = os.environ.get('COMPUTERNAME')
    g = geocoder.ip('me')
    l = str(g.citystate)
	
    d = str(datetime.datetime.now())[0]
    
    print("N:" + n)
    print("D:" + d)
    print("C:" + c)
    print("D:" + d)
    print("L:" + l)
    print("Name:" + n)
	
def printfooter(n, s):
    y = str(datetime.datetime.today().y)
    print("(c)" + year + "www." + s + ".com     " + n)

def printreport(p):
    with pdfplumber.open(p) as p:
      for page in p.pages:
        t = page.extract_t()
        print(t)