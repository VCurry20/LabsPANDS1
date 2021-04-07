# messing with OS module

import os                                        # import OS module ( file management)


filename = "amIhere.txt"                         # file name is amIHere.txt

if (os.path.exists(filename)):                   # if this file exists 
    print ("file exists")                        # print "file exists"
else:                                            # otherwise
    with open(filename, "x") as f:               # create file
        print("creating the file")               # print "creating this file"



## to run this again change the file name "amIhere.txt"