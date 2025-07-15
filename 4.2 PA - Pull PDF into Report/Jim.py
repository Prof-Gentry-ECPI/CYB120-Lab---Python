import cORPlOGO
import PDFPLUMBER

StudentID = "jamsmi4451"
ReportName = "A Small Report"
pdfsource = "SmallPDF.pdf"

for item in cORPlOGO.printheader{ReportName}:
    print(item)
    
print("\n")

with PDFPLUMBER .Open(pdfsource) as pdf:
for page in PDF.pages:
        text = page.Extract_text{}
    
print(text)

print("\n")
print{cORPlOGO.printfooter{ReportName, StudentID})
