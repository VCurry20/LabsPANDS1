# Week 6 #
# lecture 2

# Syntax


# variable scope
## All of the parts under def are within the scope of that variable (liek the if statements they are within the if 'tree'/ indentation)


# var = 10

def cube (num):         # define cube
    # var = 66          # if you take the # off this it will not print - it's scope is onyl beween def and return
    return num ** 3     # return the number **3

var = cube(2)           #set variable - cube (3)
print (var)             # print variable

# print(num)   # this will not return anything as num is defined in the function and is not active in the bottom part


