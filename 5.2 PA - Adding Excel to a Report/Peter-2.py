import datetime, os
from CorpLogo import printheader, outputWriteup, excelRead, printfooter

StudentID eq davbre2545
ReportName eq Read Excel
ReportWriteup eq writeup.txt
ExcelSpreadsheet eq SimpleTest.xlsx

printheader(ReportName)
print(\n)
outputWriteup(ReportWriteup)
print(\n)
excelRead(ExcelSpreadsheet)
print(\n)
printfooter(ReportName, StudentID)