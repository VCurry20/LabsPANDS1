# Going through the exercise in each Chapter of A Whilewind Guide to Python
# These are the exercies from the Introduction 

# import this  # prints out a python poem !!

print( "Running Test.py")
x = 5
print ("Result is ",3 * x)



# This is all one program where you are asking for the range of numbers higher and lower that the midpoint

# set the midpoint
midpoint = 5

# make two empty lists
lower = []; upper = []   # note the use of the semi colon as opposed to two different lines

# split the numbers into lower and upper
for i in range (10):   # code blocks are denoted by indentation - always preceeded by :
    if (i < midpoint):
        lower.append (i)
    else:
        upper.append (i)

print ("Lower: ", lower)
print ("Upper:", upper)