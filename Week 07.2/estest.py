# Read in a TXT File and output the numbers of e's it contains

# Week 7
# Task 7

# Veronica Curry
# Student ID: G00074924


# The program should take the file name from an argument on the command line
# read out a number - the total count of E's
# Capital / Not Capital isnt specified

## with open("GreatExpectations.TXT","r") as f:
## data = f.read (e)
## print (count(data))   

#file = open ("greatex.txt", encoding ="utf8")

with open ("greatex.txt", "r") as f:
    data = f.read()
    freq = data.count("e")
    print (freq)



# Reference 1. https://www.gutenberg.org/files/1400/1400-0.txt