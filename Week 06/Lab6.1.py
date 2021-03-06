# Lab - Functions 

# There is a quiz on this lab too - review this again like for wk 5

# Student Managament Program
# Create a program that allows a used to create and view student information
# This is broken up into parts to that is easier to digest so this might look messy


## start with writing out what it will look like

def displaymenu ():
    print ("What would you like to do?")
    print ("\t(a) Add a new student")
    print ("\t(v) View Students information")
    print ("\t (q) Quit")
    choice = input ("Type one letter (a/v/q):") .strip()

    return choice
#  test the function
choice = displaymenu ()
print (" This is the first go - You choose {}".format(choice))


