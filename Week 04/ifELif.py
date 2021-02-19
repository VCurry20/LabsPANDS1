# 4.1
# Program to show the format of an IF statement

if True: # condition
    print("condition is true") #statement
# this means that if true print " Condition is true"


if False: # condition
    print("condition is also true") #statement
# --- nothing will print from this 
# it checks down the program and does not find a false value so it prints nothing



# Showing progression of if values and their uses
if 2 == 2:
    print ( "yes the world is sane") # this will print because the state is true

if 2 == 3:
    print ( "yes the world is also sane")  # nothing will print here because the state is false- there is no option given if 2 is not equal to three 


# state with two different outcome options
# this gives an outcome for false results rater that python having no output

if 2 != 2: # 2 is not equal to 2 - prints option 2 - basically you are looking for the false value ( 2 is not equal to 2)
    print("I hope this is not being displayed!!!")
else:
    print("2 is not equal to 2 - false")


if 2 != 3: # 2 is not equal to 3 - prints option 1 - because this is a true value
    print("This is a true value and will print out!!!")
else:
    print("2 is not equal to 2 - false")


# with Variables
b = 3
if b == 2:
    print ("b is equal to 2")
else:
    print ("b is not equal to 2")



a = 2
if a != 2: 
    print("I hope this is not being displayed!!!")
else:
    print("a is not equal to 2 - false")



# Elif 
aNumber = 6   ## change this to different numbers to get different outcomes eg 9 or 5

if (aNumber % 2) == 0:  ## brackets are not needed - added for clarity
    print(aNumber, "is even")  ## another way of printing variables
elif (aNumber %3) == 0: # if the number is even this will not be checked
    print(aNumber, "is divisible by 3")
else:
    print(aNumber, "is not even or divisible by 3")

print("this will always be outputted")

# When the first outout if true (the if line) - the program will not even check the elif line and so on
# the program is looking for a true option it stops running when it finds one
