# Week 6 
# Lecture 2

# flexible arugments

# this is a statement with many arguements - i can pass in as many arguments as I like
# How is this done?

print ("hi", 55, 342, [], {})

print ("hi", 55, 342, [], {}, sep=":")


# flexible number of arguments

def average (*numbers):  # will make a list of the numbers passed in
    sumOf = sum(numbers)
    return sumOf / len(numbers)

ave = average (12, 14, 67, 80, 43)  ## you can amend this and pass in as numbers as you like // multiple arguments
print ("average is ", ave)


# flexible number of named arguments

###  need to watch this video to make sense of this

def fun( arg1 = 0, arg2 = 1 ):  # set default value 
    return arg1 - arg2

print (fun)

print ( fun( arg2 = 10, arg1= 2))

def funkyargs (**args): ## take in any numner of named arguments becuase of the ** returns as a dict
    print (args)

funkyargs (name="Joe", age = 22, courses = [])

## pass in a variable list to make a dict 

