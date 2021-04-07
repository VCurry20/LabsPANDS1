# Lab Week 7 -4  Reading a dict from a file

import json

filename = "testdict.json"

def readDict ():
    # this will throw an error if the file does not exist
    # it should really just return an empty dict
    # we can do this later
    with open(filename) as f:
        return json.load(f)


# test function
somedict = readDict ()
print (somedict)