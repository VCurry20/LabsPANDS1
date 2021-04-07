# Lab Week 7 -3  Using Json module to save a data structure

# first time this runs it will create the file

import json

filename = "testdict.json"
sample= dict(name ='fred', age ='3', grades =[1,45,67])


def writeDict (obj):
    with open(filename, 'wt') as f:    ## 'wt' - over write
        json.dump(obj,f)


# test function

writeDict(sample)