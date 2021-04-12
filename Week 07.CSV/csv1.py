# messing with CSV
# Wk 7 extra

import csv                                                    # import CSV module

print ('cvs is a pain')                                       # test this, ie if this import is ok this will print

filename = "test.csv"                                         # set variable for file 

with open(filename, "rt") as csvFile:                         # with open - file as read text
    csvReader = csv.reader(csvFile, delimiter=",")            # csvreader varible = read file / delimiter is as below
    #print (csvReader)                                        # test print
    for line in csvReader:                                    # for line in csv file 
        print(line[2])                                        # print line - will print the £rd colum of info
        print(line)                                           # print line - will print out the whole file - each line is an array / info as string inside







#"""""What is a delimiter in Python?
#Python: Split a string with multiple delimiters
#
#Note : A delimiter is a sequence of one or more characters used to specify the boundary between separate, independent regions in plain text or other data streams""""