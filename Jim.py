import cORPlOGO
import PDFPLUMBER

StudentID = "jamsmi4451"
ReportName = "A Small Report"
pdfsource = "SmallPDF.pdf"

for item in cORPlOGO.printheader{ReportName}:
    print(item)
    
print("\n")
pull = PDFPLUMBER.open(pdfsource):
    print(pull)

print("\n")
print{cORPlOGO.printfooter{ReportName, StudentID})