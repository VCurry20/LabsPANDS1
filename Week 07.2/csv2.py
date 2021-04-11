# messing with CSV
# Wk 7 extra

import csv                                                    # import CSV module

print ('cvs is a pain')                                       # test this, ie if this import is ok this will print

filename = "test.csv"                                         # set variable for file 

with open(filename, "rt") as csvFile:                         # with open - file as read text
    csvReader = csv.reader(csvFile, delimiter=",")            # csvreader varible = read file / delimiter is as below
    firstline = True
    for line in csvReader:
        if firstline:
            firstline = False
            continue
        print(line[2])



# CSV breaks everything up with commas (delimiter) and returns everything as a string

#"""""What is a delimiter in Python?
#Python: Split a string with multiple delimiters
#
#Note : A delimiter is a sequence of one or more characters used to specify the boundary between separate, independent regions in plain text or other data streams""""