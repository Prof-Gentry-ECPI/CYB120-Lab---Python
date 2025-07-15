import corplogo
import pdfplumber

StudentID = "salbre1189"
ReportName = "A Small Report"
pdfsource = "SmallPDF.pdf"

for item in corplogo.printheader{ReportName:
    print{item
    
print("\n"
      
with pdfplumber.open(pdfsource as pdf:
for page in pdf.pages:
    text = page.extract_text{

print{text

print{"\n"
print{corplogo.printfooter{ReportName, StudentID
