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
        email = line[8]
        start = email.find('@')                   # find() 22 min in video
        domain = email[start+1:]                 # slicing 
        print (domain)                              


# test the find()
# email is "email@address.com"
# print(email.find('@'))     # will you give you the number it is in the email address
# start = email.find('@')    ## this will give you @address.com
# print (email[start+1:])    ## start +1 = address.com - slicing 