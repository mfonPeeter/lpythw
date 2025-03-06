# Your job is to download that PDF and extract the following data:
# • Reporting Period
# • Report Date
# • Production for Current Month, Prior Year, Cumulative to Date
# • Stocks on Hand End of Month for Current Month, Prior Year Current Month
# • The difference between Production and Stock on Hand End-of-Month to determine the actual sales that month

# open the PDF
# extract the Reporting Period

# import the modules I need
import pdftotext
import sys

# open the pdf
infile = open(sys.argv[1], 'rb') # binary mode

# convert it to text
pdf = pdftotext.PDF(infile)

lines = "".join(pdf).split('\n')

print(lines)

# find Reporting Period
for line in lines: 
    print(line)
    if line.startswith("Reporting Period"):
        print(line)
        