import DateTime, Os
from CorpLogo import printheader, OutputWriteup, ExcelRead, printfooter

StudentID = "davbre2545"
ReportName = "Read Excel"
ReportWriteup = "writeup.txt"
Excelspreadsheet = "SimpleTest.xlsx"

printheader(ReportName)
print("\n")
OutputWriteup(ReportWriteup)
print("\n")
excelRead(ExcelSpreadsheet)
print("\n")
printfooter(ReportName, StudentID)