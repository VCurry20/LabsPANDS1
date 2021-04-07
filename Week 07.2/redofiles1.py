# redo of week7 - Messing with Files



#### hashed this out so it doesnt keep creating files
#with open(".\lecture1.txt","w") as f:   # opening with "r" only poss if file exists - "w" creates the file // ck out modes in notes
#    print("create a file")


with open("testdata.txt","rt") as f:          # print all from a file ( has a limit not sure how much)
    data = f.read()                           # we created this file manually to trial from
    print (data)

with open("testdata.txt","rt") as f:          # reads 4 characters from a file
    data = f.read(4)
    print (data)


with open("testdata.txt","rt") as f:          # read in the file data in the sentence "we got***"
    for line in f:                            # each line with output
        print ("we got:***", line)

with open("testdata.txt","rt") as f:          # read from the file into the sentence - strip all spaces 
    for line in f:
        print ("we got-:", line.strip())


#with open("output.txt", "wt") as f:           # create a file
#    f.write("Hello World \n This is a Test")  # write into file "hello ...."

with open("output.txt", "wt") as f:           # overwrites the file     ## "at" to append  
    f.write("Hello World \n This is a Test")  # write into file "hello ...."
    print("my data", file = f)                # overwrites file


#with open("..\output.txt", "wt") as f:        # create a file in the parent directory ..\ is added
#    f.write("Hello World \n This is a Test")  # write into file "hello ...."


