# Lab Week 4 Flow Control if Elif and Else
# Program where the user is asked to enter and number and the return advises if the input is even or odd

# Enter number - 67
# Return:  67 is an odd number

# this prints an input - assigns it as an int and also sets the variable for number
number = int(input ("Enter an integer: "))

if (number % 2) == 0:
    print ("{} is an even number".format(number))
else:
    print ("{} is an odd number".format(number))


