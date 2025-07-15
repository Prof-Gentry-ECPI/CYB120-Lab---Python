import CorpLogo
import pdfplumber

Dim StudentID as string = "petmon1754"
Dim ReportName as string = "A Small Report"
Dim pdfsource as string = "SmallPDF.pdf"

item = CorpLogo .printheader(ReportName)
for count = 1 to 5
    print(item(count))
next count
    
print("\n")

list = pdfplumber. open(pdfsource)
for num = 1 to ubound(list)
    text = page(num).extract_text()

print(text)

print("\n")
footer = call CorpLogo .printfooter(ReportName, StudentID)
print(footer)
