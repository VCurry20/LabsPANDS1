# Lab - Functions 

# There is a quiz on this lab too - review this again like for wk 5

# Student Managament Program
# Create a program that allows a used to create and view student information
# This is broken up into parts to that is easier to digest so this might look messy


## This is the second Amendment (3 on the lab sheet)

def displaymenu ():
    print ("What would you like to do?")
    print ("\t(a) Add a new student")
    print ("\t(v) View Students information")
    print ("\t (q) Quit")
    choice = input ("Type one letter (a/v/q):") .strip()
    return choice

def doAdd ():
    # we fill this in later
    print ("In Adding")
def doView ():
    # we fill this in later
    print ("In Viewing")

# main program

choice = displaymenu ()
while (choice != 'q'):
    # we could do this with lamda functions
    # I am keeping this basic at the moment
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice != 'q':
        print ("\n\n Please select either a, v, p")
    choice = displaymenu ()

