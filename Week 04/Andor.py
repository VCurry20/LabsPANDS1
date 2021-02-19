# 4.1 Lecture
# Messing with And's and Or's


# Using And & Or's in Phython is messy 
# We think in English but we need to think in Python when using these
# The following is an example that works in English but in Python it is a syntax error

# number = 77
# if number >=0 and <= 100:
#    print(" Valid ")

# The reason for this error is - Python does not understand what you are saying with <= 100:
# it is asking what is <= 100:? What is this referring too

# To fix this issue tell python what you are referring too

number = 77
if number >=0 and number <= 100:
    print(" Valid 1")

# Add brackets to make clearer

number = 77
if  (number >=0 ) and ( number <= 100 ):
    print(" Valid 2 ")




# Another mistake - in English eg " I don't want to do something if number is more and 100 and less than 500"
# in python this will not work like this
# go will always print
# when you use 'and' python is asking in each if statement that both conditions are true
# also in the second if - one if true and the other is false so true * false = false ( python algebra)

number =  -1
if  (number >=0 ) and ( number <= 100 ):  ## print if number is greater than 0 and less than 100
    print(" Valid 3 ")

if (number <= 0 ) and ( number >= 100 ) : ## print is number is less than 0 and greater than 100
    print ( "stop ")

else: 
    print ("go version 1") # if none apply print go


## By changing the and in the second statement to OR it will give only needs one to be true

number =  -1
if  (number >=0 ) and ( number <= 100 ):  ## print if number is greater than 0 and less than 100
    print(" Valid 3 ")

if (number <= 0 ) or ( number >= 100 ) : ## print is number is less than 0 and greater than 100
    print ( "stop version 2")

else: 
    print ("go") # if none apply print go






### AVOID AND'S AND OR'S - JUST USE IF STATEMENTS WHICH IS EASIER 
# try avoid negatives

## review the end of this lecture if you are doing this again for ifbad - so if this is not that answer something will print?
### NOT SURE ABOUT THIS REVIEW AGAIN
number =  -1
if  (number >=0 ) and ( number <= 100 ):  
    print(" Valid 4 ")

if (number <= 0 ) or ( number >= 100 ) : 
    isbad = True
    print ( "stop version 3")

else: 
    print ("go") 