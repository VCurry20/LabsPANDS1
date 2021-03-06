# Lab - Functions 

# There is a quiz on this lab too - review this again like for wk 5

# Student Managament Program
# Create a program that allows a used to create and view student information
# This is broken up into parts to that is easier to digest so this might look messy


## This is the fifth Amendment (6 on the lab sheet)

# the arry we store everything in 

def displaymenu ():
    print ("What would you like to do?")
    print ("\t(a) Add a new student")
    print ("\t(v) View Students information")
    print ("\t (q) Quit")
    choice = input ("Type one letter (a/v/q):") .strip()
    return choice

def doAdd (students) :
    currentstudent = {}
    currentstudent ["name"] = input ("enter student's name:")
    currentstudent ["modules"] = readmodules ()
    students.append (currentstudent)

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

def displaymodules (modules) :
    print ("\t name  \tGrade")
    for module in modules:
        print("\t{}  \t{}".format(module["name"], module["grade"]))

def doView(students):
    for currentstudent in students:
        print(currentstudent ["name"])
        displaymodules (currentstudent["modules"])

# main program
students = []
choice = displaymenu ()
while (choice != 'q'):
    # we could do this with lamda functions
    # I am keeping this basic at the moment
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice != 'q':
        print ("\n\n Please select either a, v, p")
    choice = displaymenu ()

