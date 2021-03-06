# Week 6 
# lecture 2

# Syntax


# variable scope
## All of the parts under def are within the scope of that variable (liek the if statements they are within the if 'tree'/ indentation)


var = 10

def cube (num):         
    var = 66     #### if i didnt not define var in the function it would look outside it for the value - # the sentence to test
    print ("This is the variable in the function", var)       
    return num ** 3    

cube(2)
print ("This is the variable outside the function", var)             

 
## you need cube(22) to get it to print

###    BE CAREFUL THAT YOU KNOW WHERE YOUR VARIABLES WILL PULL FROM AND TEST AS YOU GO