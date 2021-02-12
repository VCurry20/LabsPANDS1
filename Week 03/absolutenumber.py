# lab 3.2 Fun with Numbers
# program to give you an absolute number 
# eg. +4 or -4 = absolute number 4

# Question 2
# Enter a number = -4 / /  give the absolute value of -4.0 is 4.0

# Answer
# Return an absolute number - also return the absolute number in float form (he asks for 4.0 not just 4)

# Set variables
number = float(input(" Enter a number:"))
absoluteValue = abs(number)

# input command
print(" The absolute value of {} is {}".format(number, absoluteValue))
