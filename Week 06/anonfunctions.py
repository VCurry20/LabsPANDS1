# Week 6
# Lecture 3

# this is as an FYI and I need to go over the further reading for this to make sense
# need to watch the video with this as you need to mess with the code and see what happens in progression

def doubler (num):
    return num * 2

def tripler (num):
    return num * 3

fun = doubler   # variable set as function
fun = tripler   # variable reset as function

# var = doubler (10)
var = fun (2)  # this will act as the fucntion which as been set above
print (var) 




# This can now allow for the use of functions in if statements
# This is messy but can be done

def doublerb (num):
    return num * 2

def triplerb (num):
    return num * 3

isMax = True
if isMax:
    fun = doublerb
else:
    fun = triplerb

var = fun (10)  
print (var) 
