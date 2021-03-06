# Lab - Functions 

# There is a quiz on this lab too - review this again like for wk 5

# Student Managament Program
# Create a program that allows a used to create and view student information
# This is broken up into parts to that is easier to digest so this might look messy


## This is the forth Amendment (5 on the lab sheet)
# We need to now read in the modules

def readmodules ():
    modules = []
    modulename = input("\t Enter the first module name (blank to quit):").strip()

    while modulename != "":
        module = {}
        module ["name"] = modulename
        # i am not doing error handling
        module ["grade"] =int(input("\t\t Enter grade:"))
        modules.append(module)
        # now read the next module name
        modulename = input("\t next module name (blank to quit):").strip()


    return modules