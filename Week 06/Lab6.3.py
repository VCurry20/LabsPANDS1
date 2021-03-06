# Lab - Functions 

# There is a quiz on this lab too - review this again like for wk 5

# Student Managament Program
# Create a program that allows a used to create and view student information
# This is broken up into parts to that is easier to digest so this might look messy


## This is the third Amendment (4 on the lab sheet)

# so for this part we are writing the code for taking in the data and how to handle it - we are not thinking about the display
# just showing how parts of the code are seperately wrote and then brought together
# breaking the program down makes it easier to work out the correct approach

## write the doadd function
# read in the students name
# read in the modules and grades (will be in the next part)
# test this function to create ad DICT
# Add to this list
# Test it

students = []
def readmodules ():
    return []

def doAdd (students) :
    currentstudent = {}
    currentstudent ["name"] = input ("enter student's name:")
    currentstudent ["modules"] = readmodules ()
    students.append (currentstudent)

#test

doAdd(students)

doAdd(students)

print(students)