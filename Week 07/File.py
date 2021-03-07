# Week 7 
# Lecture 1

# Creating, Opening, amending files through python
# use the open with module for files // when using this module you never have to worry about closing the file again

# this page we create and read from a file

""" this works to create a file but cannot continue to rn it as it will continue to create files """

#with open (".\week 07.txt", "w") as f:
#    print ("create a file")

## I could have used "a" or "x" instead of "w"


# read from a file

# this will read up to the default ( so maybe not the whole file if it is huge)
with open ("Textfile", "rt") as f:
    data = f.read()
    print (data)

# this will read only 7 characters - there is characters counted for new lines
with open ("Textfile", "rt") as f:
    data = f.read(7)   ## 7 chraracters
    print (data)


# read out part of the file in a sentence
with open ("Textfile", "rt") as f:
    for line in f:
        print ("from txt file: ", line)


# reads out the text from the file but also clears away the extra spaces
with open ("Textfile", "rt") as f:
    for line in f:
        print ("from txt file: ", line.strip())  # strip function


