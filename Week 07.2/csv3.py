# Messing with CSV 
# Week 7

# Count email domains in employees csv
# This will count each email domain on the file - so how many ppl have gmail for example

import csv

filename =  "employees.csv"

with open(filename, "rt") as employeefile:
    csvreader = csv.reader(employeefile, delimiter= ',')
    firstline = True
    count = 0
    for line in csvreader:
        print(line)


#### this will print the whole file out