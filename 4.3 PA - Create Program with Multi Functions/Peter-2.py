from CorpLogo import printheader, printreport, printfooter

StudentID eq davbre2545
ReportName eq A medium report
pdfsource eq MediumPDF.pdf

printheader(ReportName)
print(\n)
printreport(pdfsource)
print(\n)
printfooter(ReportName, StudentID)