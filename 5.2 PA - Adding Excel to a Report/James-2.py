import datetime, os
from CorpLogo import printheader, outputWriteup, excelRead, printfooter

s = "davbre2545"
r = "Read Excel"
r = "writeup.txt"
e = "SimpleTest.xlsx"

printheader(r)
print("\n")
ouptutWriteup(r)
print("\n")
excelRead(e)
print("\n")
printfooter(r, s)