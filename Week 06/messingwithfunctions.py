# Week 6 Functions 
# Lecture 1 

# making a function and how to use them
# Use functions to break you code into manageable chunks and functions can be reused through out the program once defined
# When making a function think what is going into the function and the results will be or what you want them to be



def cube (num):  ## define fuction
#    print ("in cube")
    return num ** 3  ## state what it should do?

var = cube (10)  # set variable - run function
print (var)    # print variable 



# for/loop with function
for i in range (1,11):
    print( i, "cubed is :", cube(i))  # print out the cubed result of the numbers within range 1/10




