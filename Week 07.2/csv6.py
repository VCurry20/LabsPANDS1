# Messing with CSV 
# Week 7

# Count email domains in employees csv
# This will count each email domain on the file - so how many ppl have gmail for example
# Andrew counted along the file - so you are looking for column 8 (line[8]) and then the sentence details within that column

### why is it line 8 though ? and not column?

import csv

filename =  "employees.csv"
domaincount = {}

with open(filename, "rt") as employeefile:
    csvreader = csv.reader(employeefile, delimiter= ',')
    firstline = True
    count = 0
    for line in csvreader:
        if firstline:                                 # this part will make sure you do not print the first line
            firstline = False                                       
            continue
        email = line[8]
        start = email.find('@')                        # find() 22 min in video
        domain = email[start+1:]                       # slicing 
        if domain not in domaincount:                   
            domaincount[domain] = 0



print (domaincount)      # this will print out all the domain names?!