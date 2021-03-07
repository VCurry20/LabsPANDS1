# Week 6
# Lecture 3

# this is as an FYI and I need to go over the further reading for this to make sense
# need to watch the video with this as you need to mess with the code and see what happens in progression
# follow on from anonfunctions.py

"""def doublerb (num):
    return num * 2

def triplerb (num):
    return num * 3

isMax = True
if isMax:
    fun = doublerb
else:
    fun = triplerb

var = fun (10)  
print (var) """""

# another and better way to write this is as follows - 
# lambda

isMax = True
if isMax:
    fun = lambda num : num * 2   ## this is an anon function - it says this is a function it takes in one thing : and it returns is *2
else:
    fun = lambda num : num * 3

var = fun (10)  
print (var) 

