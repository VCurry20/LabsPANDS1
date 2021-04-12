# Messing with CSV 
# Week 7

# Count email domains in employees csv
# This will count each email domain on the file - so how many ppl have gmail for example
# Andrew counted along the file - so you are looking for column 8 (line[8]) and then the sentence details within that column

### why is it line 8 though ? and not column?

import csv

filename =  "employees.csv"

with open(filename, "rt") as employeefile:
    csvreader = csv.reader(employeefile, delimiter= ',')
    firstline = True
    count = 0
    for line in csvreader:
        if firstline:                                 # this part will make sure you do not print the first line
            firstline = False                                       
            continue
        print(line[8])


# this will just print all from line 8 - or column 8 in an excel - ignoring the first line
