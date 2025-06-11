import CorpLogo
import pdfplumber

Dim StudentID as string = "petmon1754"
Dim ReportName as string = "A Small Report"
Dim pdfsource as string = "SmallPDF.pdf"

item = CorpLogo .printheader(ReportName)
for count = 1 to 5
    print(item(count))
    
print("\n")

if pull = pdfplumber.open(pdfsource) then
    print(list)

print("\n")
footer = call CorpLogo .printfooter(ReportName, StudentID)
print(footer)
