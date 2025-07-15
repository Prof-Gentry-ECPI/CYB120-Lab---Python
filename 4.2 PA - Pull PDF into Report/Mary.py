import CorpLogo
import pdfplumber

StudentID = "marhyn8894
ReportName = "A Small Report'
pdfsource = 'SmallPDF.pdf"

for item in CorpLogo.printheader(ReportName):
print(item)
    
print("\n')

with pdfplumber.open(pdfsource) as pdf:
for page in pdf.pages:
text == page.extract_text()
print(text)

print("\n')
print{CorpLogo.printfooter(ReportName, StudentID))
